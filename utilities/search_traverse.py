import os
import time
import traceback
from datetime import datetime

from selenium.webdriver.common.by import By

from cl_selenium import cl_selectors, cl_scrap
from cl_selenium.cl_scrap import cl_loop_actions
from ia_selenium import ia_selectors
from ia_selenium.ia_scrap import ia_app, ia_loop_actions
from utilities.companys import companies
from utilities.web_driver import driver_setup


def scrape_traverse(confs, tables, iteration_time, company, thread_name="Non-thread"):
    """
    The thread_generator function is responsible for generating threads to scrape data from different companies. It
    creates dataframes for different tables and retrieves contract numbers for the specified company. It then
    iterates through the contract numbers, calling the scrape_traverse function to scrape data for each contract. The
    iteration continues until there are no exceptions or until the maximum number of iterations is reached.

    :param confs: Configuration dictionary
    :param tables: dataframes used for stored scarped data (for current thread)
    :param iteration_time: how many iterations to scrape if there are errors during scraping, here it is only
    for generating the log file name
    :param company: company name
    :param thread_name: the name of this thread

    :return: None

    Flow:
    # 1. Retrieve the contract numbers for the specified company.
    # 2. If there are any contract numbers in the recovery list, use them instead of the original contract numbers.
    # 3. Set up the web driver based on the configuration parameters.
    # 4. Depending on the company, initialize the necessary paths and start the corresponding application.
    # 5. Create a log file to record any exceptions that occur during scraping.
    # 6. Set the maximum reset count and initialize the counters.
    # 7. Iterate through the contract numbers.
    # 8. If the continuous error count or driver reset count exceeds the maximum values, restart the web driver.
    # 9. If the website is in an error page for the 'iA' company, go back to the root URL.
    # 10. Set up the current contract number and print a message indicating the contract being scraped.
    # 11. Call the ia_loop_actions function to perform the scraping actions for the current contract.
    # 12. Update the counters and log any exceptions that occur.
    # 13. Save the recovery list after the current traverse.
    # 14. Remove records from the tables that had exceptions during scraping.
    # 15. Close the web driver.
    # 16. Print a message indicating the completion of the scrape traverse and the total number of errors.
    """
    # keep contracts number if there is exception in the previous loop
    if len(tables['recover']) == 0:
        contracts = tables['contracts']
    else:
        contracts = tables['contracts'][tables['contracts']['Contract_number'].isin(tables['recover'])]
    # clean the recover list
    tables['recover'].clear()

    # set up the driver
    wd = driver_setup(confs)

    paths = {}
    match company:
        case 'iA':
            paths = ia_selectors.scrape_paths()
            # set up the driver and start IA page
            ia_app(wd, confs, thread_name)
        case 'CL':
            paths = cl_selectors.login_paths()
            # set up the driver and start CL page
            cl_scrap.login(wd, confs['parameters']['username'], confs['parameters']['password'])
            # initialize the cl_web and selenium paths, finish log in and go to client page.
        case 'EQ':
            # TODO: prepare paths and login eq if needed
            pass
        case '_':
            print('Company: ' + company + 'Not Found! Will Terminate the loop')
            exit()

    # generate the log file name to record the exceptions
    logfile = os.path.join(confs['csvs'], "error_log_" + thread_name + "_" + str(iteration_time) + ".txt")

    # set uo the max reset count
    max_reset_count = 25
    max_error_reset_count = 5
    # initialize the counters
    loop_continuous_error = 0
    driver_reset_count = 0
    error_count = 0
    with open(logfile, 'a') as log:
        for index, row in contracts.iterrows():
            # if the counter exceed the max values, restart the web driver
            if loop_continuous_error > max_error_reset_count or driver_reset_count >= max_reset_count:
                wd.close()
                wd = driver_setup(confs)
                match company:
                    case 'iA':
                        ia_app(wd, confs, thread_name)
                    case 'CL':
                        cl_scrap.login(wd, confs['parameters']['username'], confs['parameters']['password'])
                        # initialize the app
                    case 'EQ':
                        # TODO: prepare paths and login eq if needed
                        pass

                loop_continuous_error = 0
                driver_reset_count = 0
            # iA: if the website is in error page, get to the root url
            try:
                if company == companies['iA'] and len(wd.find_elements(By.XPATH, paths['error_page'])) != 0:
                    print(f"{thread_name} Error happens: Website crash")
                    time.sleep(5)
                    wd.get(confs['parameters']['web_url'])
            except Exception as e:
                log.write(f"{thread_name} Error: iA - website page\n")
                log.write(str(e))
                log.write(traceback.format_exc())

            # set up the current contract number
            contract_number_ = row['Contract_number']
            print(f"{thread_name} - {datetime.now()}: scrapping for contract number {contract_number_}")

            try:
                # go to clients and search for contract number
                match company:
                    case 'iA':
                        ia_loop_actions(wd, paths, confs, contract_number_, tables, row['Contract_start_date'])
                    case 'CL':
                        cl_loop_actions(wd, paths, confs, contract_number_, tables)
                    case 'EQ':
                        # TODO: perform the actions
                        pass

                loop_continuous_error = 0
                driver_reset_count += 1
            except Exception as e:
                loop_continuous_error += 1
                error_count += 1
                print(f"{thread_name} Error: Scrape interrupted on customer: {contract_number_}")
                tables['recover'].append(contract_number_)

                log.write(f"{thread_name} Error: Scrape interrupted on customer: {contract_number_}\n")
                log.write(str(e))
                log.write(traceback.format_exc())
                log.write("=============================================================\n")

    # save recovery list after current traverse
    recovery = os.path.join(confs['csvs'], "recovery_list_" + thread_name + "_" + str(iteration_time) + ".txt")
    with open(recovery, 'a') as f:
        for item in tables['recover']:
            # write each item on a new line
            f.write(str(item) + '\n')

    # remove records that there are exceptions
    if confs['control_unit'] & 1:
        tables['saving'] = tables['saving'][~tables['saving']['Contract_number'].isin(tables['recover'])]
        tables['fund'] = tables['fund'][~tables['fund']['Contract_number'].isin(tables['recover'])]
    if confs['control_unit'] & 2:
        tables['transaction'] = tables['transaction'][~tables['transaction']['Contract_number'].isin(tables['recover'])]
    if confs['control_unit'] & 4:
        tables['beneficiary'] = tables['beneficiary'][~tables['beneficiary']['Contract_number'].isin(tables['recover'])]
        tables['participant'] = tables['participant'][~tables['participant']['Contract_number'].isin(tables['recover'])]
        tables['client'] = tables['client'][~tables['client']['Contract_number_as_owner'].isin(tables['recover'])]

    wd.close()

    print(f"{thread_name} {datetime.now()}: scrape traverse complete")
    print(f"{thread_name} Total error during scrape: {error_count}")
    print("=========================")