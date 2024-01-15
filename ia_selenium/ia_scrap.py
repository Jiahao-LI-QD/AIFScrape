import os.path
import time
import traceback

import os
import shutil
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from ia_selenium import ia_login, ia_investment, ia_transactions, ia_client
from dbutilities import dbColumns, ia_db
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from dbutilities import connection
from ia_selenium import ia_selectors

def driver_setup(parameters):
    # start web driver
    chrome_options = webdriver.ChromeOptions()
    prefs = {'download.default_directory': os.path.join(parameters['csv_path'], parameters['contracts'])}
    chrome_options.add_experimental_option('prefs', prefs)
    wd = webdriver.Chrome(chrome_options)
    wd.implicitly_wait(15)
    return wd

def ia_app(wd, parameters):
    # get the url and login
    wd.get(parameters['web_url'])

    ia_login.login(wd, parameters['username'], parameters['password'])
    paths = ia_selectors.scrape_paths()
    # accept cookie
    time.sleep(1)
    wait = WebDriverWait(wd, 10)  # seconds want to wait
    wait.until(
        EC.element_to_be_clickable((By.XPATH, paths['cookie_button']))
    ).click()


def create_table(control_unit):
    # create pointers
    result = {'saving': pd.DataFrame(columns=dbColumns.saving_columns),
              'fund': pd.DataFrame(columns=dbColumns.fund_columns),
              'transaction': pd.DataFrame(columns=dbColumns.transaction_columns),
              'beneficiary': pd.DataFrame(columns=dbColumns.beneficiary_columns),
              'participant': pd.DataFrame(columns=dbColumns.participant_columns),
              'client': pd.DataFrame(columns=dbColumns.client_columns)}
    return result


def scrape_traverse(wd, control_unit, tables, csvs, iteration_time, parameters):
    paths = ia_selectors.scrape_paths()
    error_count = 0
    error_contract_number = 0
    if len(tables['recover']) == 0:
        contracts = tables['contracts']
    else:
        contracts = tables['contracts'][tables['contracts']['Contract_number'].isin(tables['recover'])]
    # clean the recover list
    tables['recover'].clear()

    logfile = os.path.join(csvs, "error_log_" + str(iteration_time) + ".txt")
    with open(logfile, 'a') as log:
        for index, row in contracts.iterrows():
            if len(wd.find_elements(By.XPATH, "/html/body/div[1]/ee-header-fullpage/div/div[1]/span/div[1]/div")) != 0:
                print("Error happens: Website crash")
                time.sleep(5)
                wd.get(parameters['web_url'])
            contract_number_ = row['Contract_number']
            print(f"scrapping for contract number {contract_number_}")

            try:
                wd.find_element(By.XPATH, paths['myclient_button']).click()

                wd.find_element(By.XPATH, paths['contract_number_input']).clear()

                wd.find_element(By.XPATH, paths['contract_number_input']).send_keys(contract_number_)

                wd.find_element(By.XPATH, paths['search_button']).click()
            except Exception as e:
                error_contract_number += 1
                print(f"Error: Cannot found customer: {contract_number_}")

                log.write(f"Error: Cannot found customer: {contract_number_}\n")
                log.write(str(e))
                log.write(traceback.format_exc())
                log.write("=============================================================\n")

                tables['recover'].append(contract_number_)
                continue

            try:
                if control_unit & 1:
                    ia_investment.scrape_investment(wd, tables['fund'], tables['saving'])
                if control_unit & 2:
                    ia_transactions.scrape_transaction(wd, tables['transaction'], row['Contract_start_date'])
                if control_unit & 4 or contract_number_ in tables['new_contracts']:
                    ia_client.scrape(wd, tables['client'], tables['beneficiary'], tables['participant'],
                                     contract_number_)
            except Exception as e:
                print(f"Error: Scrape interrupted on customer: {contract_number_}")
                tables['recover'].append(contract_number_)
                error_count += 1

                log.write(f"Error: Scrape interrupted on customer: {contract_number_}\n")
                log.write(str(e))
                log.write(traceback.format_exc())
                log.write("=============================================================\n")

    # save recovery list after current traverse
    recovery = os.path.join(csvs, "recovery_list_" + str(iteration_time) + ".txt")
    with open(recovery, 'a') as f:
        for item in tables['recover']:
            # write each item on a new line
            f.write(item + '\n')

    if control_unit & 1:
        tables['saving'] = tables['saving'][~tables['saving']['Contract_number'].isin(tables['recover'])]
        tables['fund'] = tables['fund'][~tables['fund']['Contract_number'].isin(tables['recover'])]
    if control_unit & 2:
        tables['transaction'] = tables['transaction'][~tables['transaction']['Contract_number'].isin(tables['recover'])]
    if control_unit & 4 or contract_number_ in tables['new_contracts']:
        tables['beneficiary'] = tables['beneficiary'][~tables['beneficiary']['Contract_number'].isin(tables['recover'])]
        tables['participant'] = tables['participant'][~tables['participant']['Contract_number'].isin(tables['recover'])]
        tables['client'] = tables['client'][~tables['client']['Contract_number'].isin(tables['recover'])]

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
    if control_unit & 4 or len(tables['new_contracts']) != 0:
        tables['client'].to_csv(files['client'])
        tables['beneficiary'].to_csv(files['beneficiary'])
        tables['participant'].to_csv(files['participant'])
    tables['contracts'].to_csv(files['contracts'])

    print("CSVs saved!")
    print("=========================")


def save_csv_to_db(control_unit, files, new_contracts):
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
        if control_unit & 4 or new_contracts:
            # delete current client information related tables for later insertion
            # if there is no new contracts
            # otherwise just extend the table
            if not new_contracts:
                ia_db.delete_current_participant_beneficiary(cursor)
                ia_db.delete_current_client(cursor)
            ia_db.save_data_into_db(cursor, files['client'], ia_db.save_client_history, batch_size)
            ia_db.save_data_into_db(cursor, files['participant'], ia_db.save_participant_history, batch_size)
            ia_db.save_data_into_db(cursor, files['beneficiary'], ia_db.save_beneficiary_history, batch_size)

        # save current tables accordingly
        if control_unit & 4 or new_contracts:
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

    print("Saving to Databases")
    print("=========================")


## fetch contracts_current table from SQL Server to compare with newly downloaded contract excel file.
def check_new_clients(tables):
    try:
        cursor = connection.connect_db().cursor()
    except Exception as e:
        print(e)
        print("Database connection failed!")
    else:
        print("Database connection successful!")

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
        print('new_client_df')
        print(tables['new_contracts'])

        cursor.close()


def click_contract_list(wd):
    paths = ia_selectors.download_path()
    wd.find_element(By.XPATH, paths['myclient_button']).click()
    wd.find_element(By.XPATH, paths['download_option']).click()
    wd.find_element(By.XPATH, paths['search_button']).click()
    wd.find_element(By.XPATH, paths['submit_button']).click()
    print('Download successfully submitted')
    pass


def save_contract_list(wd, parameters, date_today):
    paths = ia_selectors.save_path()

    wd.find_element(By.XPATH, paths['mailbox_button']).click()
    wd.find_element(By.XPATH, paths['file_link']).click()
    wd.find_element(By.XPATH, paths['download_file']).click()
    filename = wd.find_element(By.XPATH, paths['download_file']).text
    time.sleep(3)

    def rename_downloaded_file(old_name, new_name):
        # Check if the file exists
        if os.path.exists(old_name):
            # Rename the file
            os.rename(old_name, new_name)
            print(f"File {old_name} renamed to {new_name}")
        else:
            print(f"File {old_name} does not exist")

    # Provide the old and new file names
    result = date_today + '_contract.XLSX'
    new_filename = os.path.join(parameters['csv_path'], parameters['contracts'],
                                result)  # Replace with the desired new file name
    old_file = os.path.join(parameters['csv_path'], parameters['contracts'], filename)

    rename_downloaded_file(old_file, new_filename)

    print('Rename file passed')
    return result
