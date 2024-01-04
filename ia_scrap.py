import os.path
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from ia_load import save_data_into_db
from ia_selenium import ia_login, ia_investment, ia_transactions, ia_client
from dbutilities import dbColumns, ia_db
import pandas as pd
from ia_selenium import keys
from selenium.webdriver.support import expected_conditions as EC
from dbutilities import connection
from ia_selenium import ia_selectors

# required parameters for app
try:
    parameters = keys.ia_account()
except Exception as e:
    print(e)
    exit()

# start web driver
wd = webdriver.Chrome()

wd.implicitly_wait(15)

wd.get(parameters['web_url'])

ia_login.login(wd, parameters['username'], parameters['password'])
paths = ia_selectors.scrape_paths()
# accept cookie
# accept cookie
time.sleep(1)
wait = WebDriverWait(wd, 10)  # seconds want to wait
wait.until(
    EC.element_to_be_clickable((By.XPATH, paths['cookie_button']))
).click()

contracts = pd.read_excel(os.path.join(parameters['csv_path'], parameters['contracts']))
contracts.columns = dbColumns.contract_columns

# create pointers
client = pd.DataFrame(columns=dbColumns.client_columns)
saving = pd.DataFrame(columns=dbColumns.saving_columns)
beneficiary = pd.DataFrame(columns=dbColumns.beneficiary_columns)
participant = pd.DataFrame(columns=dbColumns.participant_columns)
transaction = pd.DataFrame(columns=dbColumns.transaction_columns)
fund = pd.DataFrame(columns=dbColumns.fund_columns)


for index, row in contracts.iloc[2:].iterrows():
    print(f"scrapping for contract number {row['Contract_number']}")
    # TODO: Control Unit
    try:
        wd.find_element(By.XPATH, paths['myclient_button']).click()

        wd.find_element(By.XPATH, paths['contract_number_input']).clear()

        wd.find_element(By.XPATH, paths['contract_number_input']).send_keys(row['Contract_number'])

        wd.find_element(By.XPATH, paths['search_button']).click()

        ia_investment.scrape_investment(wd, fund, saving)

        ia_transactions.scrape_transaction(wd, transaction, row['Contract_start_date'])

        ia_client.scrape(wd, client, beneficiary, participant)
    except Exception as e:
        print(e)
        print(f"something happens when account number is {row['Contract_number']}")

print("scrape complete")
print("=========================")
fund.to_csv(os.path.join(parameters['csv_path'],'funds.csv'))
saving.to_csv(os.path.join(parameters['csv_path'],'savings.csv'))
transaction.to_csv(os.path.join(parameters['csv_path'],'transactions.csv'))
client.to_csv(os.path.join(parameters['csv_path'],'clients.csv'))
beneficiary.to_csv(os.path.join(parameters['csv_path'],'beneficiaries.csv'))
participant.to_csv(os.path.join(parameters['csv_path'],'participants.csv'))
contracts.iloc[2:].to_csv(os.path.join(parameters['csv_path'],'contracts.csv'))
print("Saving to CSVS")
print("=========================")


try:
    cursor = connection.connect_db().cursor()
except Exception as e:
    print(e)
    print("Database connection failed!")
else:
    print("Database connection successful!")
    size = 1000
    save_data_into_db(cursor, os.path.join(parameters['csv_path'],'clients.csv'), ia_db.save_client_history, 1000)

    save_data_into_db(cursor, os.path.join(parameters['csv_path'],'participants.csv'), ia_db.save_participant, 1000)

    save_data_into_db(cursor, os.path.join(parameters['csv_path'],'beneficiaries.csv'), ia_db.save_beneficiary, 1000)

    save_data_into_db(cursor, os.path.join(parameters['csv_path'],'savings.csv'), ia_db.save_saving_history, 1000)

    save_data_into_db(cursor, os.path.join(parameters['csv_path'],'funds.csv'), ia_db.save_fund_history, 1000)

    save_data_into_db(cursor, os.path.join(parameters['csv_path'],'transactions.csv'), ia_db.save_transaction, 1000)

    save_data_into_db(cursor, os.path.join(parameters['csv_path'],'contracts.csv'), ia_db.save_contract, 1000)

print("Saving to Databases")
print("=========================")

