import os.path
import time
import traceback

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from ia_selenium import ia_login, ia_investment, ia_transactions, ia_client
from dbutilities import dbColumns, ia_db
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from dbutilities import connection
from ia_selenium import ia_selectors


def ia_app(parameters):
    # start web driver
    wd = webdriver.Chrome()

    wd.implicitly_wait(15)

    wd.get(parameters['web_url'])

    ia_login.login(wd, parameters['username'], parameters['password'])
    paths = ia_selectors.scrape_paths()
    # accept cookie
    time.sleep(1)
    wait = WebDriverWait(wd, 10)  # seconds want to wait
    wait.until(
        EC.element_to_be_clickable((By.XPATH, paths['cookie_button']))
    ).click()

    return wd


def create_table(control_unit):
    # create pointers
    result = {}
    if control_unit & 1:
        result['saving'] = pd.DataFrame(columns=dbColumns.saving_columns)
        result['fund'] = pd.DataFrame(columns=dbColumns.fund_columns)
    if control_unit & 2:
        result['transaction'] = pd.DataFrame(columns=dbColumns.transaction_columns)
    if control_unit & 4:
        result['beneficiary'] = pd.DataFrame(columns=dbColumns.beneficiary_columns)
        result['participant'] = pd.DataFrame(columns=dbColumns.participant_columns)
        result['client'] = pd.DataFrame(columns=dbColumns.client_columns)
    return result


def scrape_traverse(wd, control_unit, tables, csvs, iteration_time):
    paths = ia_selectors.scrape_paths()
    error_count = 0
    error_contract_number = 0
    if len(tables['recover']) == 0:
        contracts = tables['contracts']
    else:
        contracts = tables['contracts'][tables['contracts']['contract_number'].isin(tables['recover'])]
    # clean the recover list
    tables['recover'].clear()

    # TODO: create error log file
    logfile = os.path.join(csvs, "error_log_" + iteration_time + ".txt")
    with open(logfile, 'a') as log:
        for index, row in contracts.iterrows():
            print(f"scrapping for contract number {row['Contract_number']}")

            try:
                wd.find_element(By.XPATH, paths['myclient_button']).click()

                wd.find_element(By.XPATH, paths['contract_number_input']).clear()

                wd.find_element(By.XPATH, paths['contract_number_input']).send_keys(row['Contract_number'])

                wd.find_element(By.XPATH, paths['search_button']).click()
            except Exception as e:
                error_contract_number += 1
                print(f"Error: Cannot found customer: {row['Contract_number']}")

                log.write(f"Error: Cannot found customer: {row['Contract_number']}")
                log.write(str(e))
                log.write(traceback.format_exc())
                log.write("=============================================================")

                tables['recover'].append(row['Contract_number'])
                continue

            try:
                if control_unit & 1:
                    ia_investment.scrape_investment(wd, tables['fund'], tables['saving'])
                if control_unit & 2:
                    ia_transactions.scrape_transaction(wd, tables['transaction'], row['Contract_start_date'])
                if control_unit & 4:
                    ia_client.scrape(wd, tables['client'], tables['beneficiary'], tables['participant'])
            except Exception as e:
                print(f"Error: Scrape interrupted on customer: {row['Contract_number']}")
                tables['recover'].append(row['Contract_number'])
                error_count += 1

                log.write(f"Error: Scrape interrupted on customer: {row['Contract_number']}")
                log.write(str(e))
                log.write(traceback.format_exc())
                log.write("=============================================================")

    # save recovery list after current traverse
    recovery = os.path.join(csvs, "recovery_list_" + iteration_time + ".txt")
    with open(recovery, 'a') as f:
        for item in tables['recover']:
            # write each item on a new line
            f.write(item)
    # TODO: clean the related record in tables

    print("scrape traverse complete")
    print(f"Total contract not found: {error_contract_number}")
    print(f"Total error during scrape: {error_count}")
    print("=========================")


def save_table_into_csv(control_unit, tables, files):

    print("Saving to CSVS")
    if control_unit & 1:
        tables['fund'].to_csv(files['fund'])
        tables['saving'].to_csv(files['saving'])
    if control_unit & 2:
        tables['transaction'].to_csv(files['transaction'])
    if control_unit & 4:
        tables['client'].to_csv(files['client'])
        tables['beneficiary'].to_csv(files['beneficiary'])
        tables['participant'].to_csv(files['participant'])
    tables['contracts'].to_csv(files['contracts'])

    print("CSVs saved!")
    print("=========================")


def save_csv_to_db(control_unit, files):
    # change file read to file paths
    try:
        cursor = connection.connect_db().cursor()
    except Exception as e:
        print(e)
        print("Database connection failed!")
    else:
        print("Database connection successful!")
        batch_size = 1000
        ia_db.save_data_into_db(cursor, files['contracts'], ia_db.save_contract_history, batch_size)
        if control_unit & 1:
            ia_db.save_data_into_db(cursor, files['saving'], ia_db.save_saving_history, batch_size)
            ia_db.save_data_into_db(cursor, files['fund'], ia_db.save_fund_history, batch_size)
        if control_unit & 2:
            ia_db.save_data_into_db(cursor, files['transaction'], ia_db.save_transaction_history, batch_size)
        if control_unit & 4:
            ia_db.save_data_into_db(cursor, files['participant'], ia_db.save_participant_history, batch_size)
            ia_db.save_data_into_db(cursor, files['beneficiary'], ia_db.save_beneficiary_history, batch_size)
            ia_db.save_data_into_db(cursor, files['client'], ia_db.save_client_history, batch_size)
    # TODO: Clear the current tables & insert current data

    print("Saving to Databases")
    print("=========================")


def click_contract_list(wd):
    # TODO: click new contract list
    pass


def save_contract_list(wd):
    # TODO: download contract list file and move to destination & rename it with current date
    pass
