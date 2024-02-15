import os
import time
import traceback
from datetime import datetime

from selenium.webdriver.common.by import By

from ia_selenium import ia_selectors
from ia_selenium.ia_scrap import ia_app, ia_loop_actions
from utilities.companys import companies
from utilities.web_driver import driver_setup


def scrape_traverse(confs, tables, iteration_time, company, thread_name="Non-thread"):
    # keep contracts number if there is exception in the previous loop
    if len(tables['recover']) == 0:
        contracts = tables['contracts']
    else:
        contracts = tables['contracts'][tables['contracts']['Contract_number'].isin(tables['recover'])]
    # clean the recover list
    tables['recover'].clear()

    # set up the driver
    wd = driver_setup(confs['parameters'])

    match company:
        case 'iA':
            paths = ia_selectors.scrape_paths()
            # set up the driver and start IA page
            ia_app(wd, confs['parameters'], thread_name)
        case 'CL':
            # TODO: initialize the ia_web and selenium paths
            pass

    # generate the log file name to record the exceptions
    logfile = os.path.join(confs['csvs'], "error_log_" + thread_name + "_" + str(iteration_time) + ".txt")

    # set uo the max reset count
    max_reset_count = 50
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
                wd = driver_setup(confs['parameters'])
                match company:
                    case 'iA':
                        ia_app(wd, confs['parameters'], thread_name)
                    case 'CL':
                        # TODO: initialize the app
                        pass

                loop_continuous_error = 0
                driver_reset_count = 0
            # iA: if the website is in error page, get to the root url
            if company == companies['iA'] and len(wd.find_elements(By.XPATH, paths['error_page'])) != 0:
                print(f"{thread_name} Error happens: Website crash")
                time.sleep(5)
                wd.get(confs['parameters']['web_url'])

            # set up the current contract number
            contract_number_ = row['Contract_number']
            print(f"{thread_name} - {datetime.now()}: scrapping for contract number {contract_number_}")

            try:
                # go to clients and search for contract number
                match company:
                    case 'iA':
                        ia_loop_actions(wd, paths, confs, contract_number_, tables, row['Contract_start_date'])
                    case 'CL':
                        # TODO: follow the ia_loop_actions, put the action of CL into one method
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