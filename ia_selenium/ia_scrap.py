import os.path
import time
import traceback

import os
from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from ia_selenium import ia_login, ia_investment, ia_transactions, ia_client
from dbutilities import db_method

from selenium.webdriver.support import expected_conditions as EC
from dbutilities import connection
from ia_selenium import ia_selectors
from utilities.tables_utilities import create_table
from utilities.web_driver import driver_setup


def ia_app(wd, parameters, thread_name="Main", recursive=0):
    """
    Getting website, and logging in .

    :param wd: represents webdriver
    :param parameters:"parameters" is getting from in ia_conf
    :param thread_name: Name of the thread (default is "Main").
    :param recursive:Indicates the number of recursive attempts (default is 0).
    :return:

    Flow:
    1. navigates to the specified web URL using the webdriver.
    2.It checks if the login button is present on the page. If not, it means the user is already logged in.
    3.If the login button is present, the function calls the ia_login function to perform the login process
    4.After logging in, the function waits for the cookie consent button to be clickable and clicks it to accept the cookies.
    5.If an exception occurs during the login process, the function will recursively try again up to 5 times.
      If it still fails, the webdriver is closed and a new one is set up before retrying.
    """

    # get the url and login
    try:
        paths = ia_selectors.scrape_paths()
        wd.get(parameters['web_url'])
        if len(wd.find_elements(By.XPATH, paths['myclient_button'])) == 0:
            ia_login.login(wd, parameters['username'], parameters['password'], thread_name)
        # accept cookie
        time.sleep(2)
        if len(wd.find_elements(By.CSS_SELECTOR, paths['cookie_consent'])) > 0:
            wait = WebDriverWait(wd, 10)  # seconds want to wait
            wait.until(
                EC.element_to_be_clickable((By.XPATH, paths['cookie_button']))
            ).click()
    except Exception as e:
        # print(e)
        # print(traceback.format_exc())
        print(f"{thread_name}: Exception during login to IA, Will Try Again")
        if recursive < 5:
            ia_app(wd, parameters, thread_name, recursive=(recursive + 1))
        else:
            wd.close()
            wd = driver_setup(parameters)
            ia_app(wd, parameters, thread_name)


def scrape_traverse(confs, tables, iteration_time, thread_name="Non-thread"):
    # parameters setting
    max_reset_count = 50
    max_error_reset_count = 5

    paths = ia_selectors.scrape_paths()
    error_count = 0
    error_contract_number = 0
    if len(tables['recover']) == 0:
        contracts = tables['contracts']
    else:
        contracts = tables['contracts'][tables['contracts']['Contract_number'].isin(tables['recover'])]
    # clean the recover list
    tables['recover'].clear()
    wd = driver_setup(confs['parameters'])
    ia_app(wd, confs['parameters'], thread_name)
    logfile = os.path.join(confs['csvs'], "error_log_" + thread_name + "_" + str(iteration_time) + ".txt")
    loop_continuous_error = 0
    driver_reset_count = 0
    with open(logfile, 'a') as log:
        for index, row in contracts.iterrows():
            if loop_continuous_error > max_error_reset_count or driver_reset_count >= max_reset_count:
                wd.close()
                wd = driver_setup(confs['parameters'])
                ia_app(wd, confs['parameters'], thread_name)
                loop_continuous_error = 0
                driver_reset_count = 0
            if len(wd.find_elements(By.XPATH, paths['error_page'])) != 0:
                print("Error happens: Website crash")
                time.sleep(5)
                wd.get(confs['parameters']['web_url'])
            contract_number_ = row['Contract_number']
            print(f"{thread_name} - {datetime.now()}: scrapping for contract number {contract_number_}")

            try:
                wd.find_element(By.XPATH, paths['myclient_button']).click()

                wd.find_element(By.XPATH, paths['contract_number_input']).clear()

                wd.find_element(By.XPATH, paths['contract_number_input']).send_keys(contract_number_)

                wd.find_element(By.XPATH, paths['search_button']).click()
            except Exception as e:
                loop_continuous_error += 1
                error_contract_number += 1
                print(f"{thread_name} Error: Cannot found customer: {contract_number_}")

                log.write(f"{thread_name} Error: Cannot found customer: {contract_number_}\n")
                log.write(str(e))
                log.write(traceback.format_exc())
                log.write("=============================================================\n")

                tables['recover'].append(contract_number_)
                continue

            try:
                if confs['control_unit'] & 1:
                    ia_investment.scrape_investment(wd, tables['fund'], tables['saving'])
                if confs['control_unit'] & 2:
                    ia_transactions.scrape_transaction(wd, tables['transaction'], row['Contract_start_date'])
                if confs['control_unit'] & 4:
                    ia_client.scrape(wd, tables['client'], tables['beneficiary'], tables['participant'],
                                     contract_number_)
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
    print(f"{thread_name} Total contract not found: {error_contract_number}")
    print(f"{thread_name} Total error during scrape: {error_count}")
    print("=========================")


def save_csv_to_db(control_unit, files, tables):
    # change file read to file paths
    try:
        cursor = connection.connect_db().cursor()
    except Exception as e:
        print(e)
        print("Database connection failed!")
    else:
        print("Database connection successful!")
        batch_size = 1000
        ia_db.save_recover(cursor, zip(tables['recover'], [None] * len(tables['recover'])))
        ia_db.save_data_into_db(cursor, files['contracts'], ia_db.save_contract_history, batch_size)
        ia_db.delete_current_contract(cursor)

        if control_unit & 1:
            # delete current table of fund & saving for later insertion
            ia_db.delete_current_fund_saving(cursor)

            # save saving & fund history
            ia_db.save_data_into_db(cursor, files['saving'], ia_db.save_saving_history, batch_size)
            ia_db.save_data_into_db(cursor, files['fund'], ia_db.save_fund_history, batch_size)
        if control_unit & 2:
            # delete current table of transaction for later insertion
            ia_db.delete_current_transaction(cursor)

            # save transaction history
            ia_db.save_data_into_db(cursor, files['transaction'], ia_db.save_transaction_history, batch_size)
        if control_unit & 4:
            # delete current client information related tables for later insertion
            # if there is no new contracts
            # otherwise just extend the table
            # if not new_contracts:
            ia_db.delete_current_participant_beneficiary(cursor)
            ia_db.delete_current_client(cursor)
            ia_db.save_data_into_db(cursor, files['client'], ia_db.save_client_history, batch_size)
            ia_db.save_data_into_db(cursor, files['participant'], ia_db.save_participant_history, batch_size)
            ia_db.save_data_into_db(cursor, files['beneficiary'], ia_db.save_beneficiary_history, batch_size)

        # save current tables accordingly
        if control_unit & 4:
            ia_db.save_data_into_db(cursor, files['client'], ia_db.save_client, batch_size)
            ia_db.save_data_into_db(cursor, files['participant'], ia_db.save_participant, batch_size)
            ia_db.save_data_into_db(cursor, files['beneficiary'], ia_db.save_beneficiary, batch_size)
        if control_unit & 1:
            ia_db.save_data_into_db(cursor, files['saving'], ia_db.save_saving, batch_size)
            ia_db.save_data_into_db(cursor, files['fund'], ia_db.save_fund, batch_size)
        if control_unit & 2:
            ia_db.save_data_into_db(cursor, files['transaction'], ia_db.save_transaction, batch_size)
        ia_db.save_data_into_db(cursor, files['contracts'], ia_db.save_contract, batch_size)

        cursor.close()

    print(f"{datetime.now()}: Saving to Databases")
    print("=========================")


## fetch contracts_current table from SQL Server to compare with newly downloaded contract excel file.
def check_new_clients(tables):
    try:
        cursor = connection.connect_db().cursor()
    except Exception as e:
        print(e)
        print(f"{datetime.now()}: Database connection failed!")
    else:
        print(f"{datetime.now()}: Database connection successful!")

        # Query & saving the SQL table into a pd dataframe.
        # conn = connection.connect_db()
        ia_db.read_clients(cursor)
        clients = [client[-2] for client in cursor.fetchall()]

        # keeping only the unique contract number row.
        csv_contract_unique_df = tables['contracts'].drop_duplicates(subset=['Contract_number'], keep='first')
        # creating new dataframe with only the new client and getting the list of contract number.
        new_client_df = csv_contract_unique_df[
            ~csv_contract_unique_df['Contract_number'].isin(clients)]
        tables['new_contracts'] = new_client_df['Contract_number'].tolist()
        # print('new_client_df')
        # print(tables['new_contracts'])

        cursor.close()


def ia_threading(confs, thread_name, contract_file):
    # start the ia company scrapy process

    # create dataframes for all the tables
    # and get contract numbers for ia company
    tables = create_table(contract_file, 'ia', True)
    # do - while loop to traverse through the contract numbers until no exception
    iteration_time = 0
    while iteration_time < confs['maximum_iteration']:
        scrape_traverse(confs, tables, iteration_time, thread_name)
        if len(tables['recover']) == 0:
            break
        iteration_time += 1
    tables['contracts'] = tables['contracts'][~tables['contracts']['Contract_number'].isin(tables['recover'])]
    confs['threading_tables'][thread_name] = tables


def scrape_cleanup(tables):
    """
    removes rows from the 'contracts' table on the 'Contract_number' column that are present in the 'recover' table.
    :param tables: a dictionary containing the 'contracts' and 'recover' tables
    :return: None, updated the 'contracts' table.
    """
    tables['contracts'] = tables['contracts'][~tables['contracts']['Contract_number'].isin(tables['recover'])]
