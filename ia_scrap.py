import os.path
import sys
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

## control unit
control_unit = 1
start_contract = None
if len(sys.argv) > 1:
    control_unit = sys.argv[1]
if len(sys.argv) > 2:
    start_contract = sys.argv[2]
if control_unit not in [1, 2, 3]:
    print(f"The control model is not supported")

if control_unit == 1:
    print("Task: Scrape Investments")
elif control_unit == 2:
    print("Task: Transactions")
else:
    print("Task: Clients Information")
print("======================")

# required parameters for app
try:
    parameters = keys.ia_account()
except Exception as e:
    print(e)
    exit()

contracts = pd.read_excel(os.path.join(parameters['csv_path'], parameters['contracts']))
# print(type(contracts))
# print(type(contracts.columns))
contracts.columns = dbColumns.contract_columns
start_index = 2
if start_contract is not None:
    indexes = contracts[contracts.Contract_number == start_contract].index
    if len(indexes) == 0:
        print("The contract number doesn't exist")
        exit()
    start_index = contracts[contracts.Contract_number == start_contract].index.values[0]
    print(f"Starting from contract number {start_contract}")
else:
    print("Scraping all contract from beginning")
print("======================")


# start web driver
wd = webdriver.Chrome()

wd.implicitly_wait(5)

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


# create pointers
if control_unit == 1:
    saving = pd.DataFrame(columns=dbColumns.saving_columns)
    fund = pd.DataFrame(columns=dbColumns.fund_columns)
elif control_unit == 2:
    transaction = pd.DataFrame(columns=dbColumns.transaction_columns)
else:
    beneficiary = pd.DataFrame(columns=dbColumns.beneficiary_columns)
    participant = pd.DataFrame(columns=dbColumns.participant_columns)
    client = pd.DataFrame(columns=dbColumns.client_columns)


for index, row in contracts.iloc[start_index:].iterrows():
    print(f"scrapping for contract number {row['Contract_number']}")

    try:
        wd.find_element(By.XPATH, paths['myclient_button']).click()

        wd.find_element(By.XPATH, paths['contract_number_input']).clear()

        wd.find_element(By.XPATH, paths['contract_number_input']).send_keys(row['Contract_number'])

        wd.find_element(By.XPATH, paths['search_button']).click()

        if control_unit == 1:
            ia_investment.scrape_investment(wd, fund, saving)
        elif control_unit == 2:
            ia_transactions.scrape_transaction(wd, transaction, row['Contract_start_date'])
        else:
            ia_client.scrape(wd, client, beneficiary, participant)
    except Exception as e:
        print(e)
        print(f"something happens when account number is {row['Contract_number']}")

print("scrape complete")
print("=========================")
if control_unit == 1:
    fund.to_csv(os.path.join(parameters['csv_path'],'funds.csv'))
    saving.to_csv(os.path.join(parameters['csv_path'],'savings.csv'))
elif control_unit == 2:
    transaction.to_csv(os.path.join(parameters['csv_path'],'transactions.csv'))
else:
    client.to_csv(os.path.join(parameters['csv_path'], 'clients.csv'))
    beneficiary.to_csv(os.path.join(parameters['csv_path'], 'beneficiaries.csv'))
    participant.to_csv(os.path.join(parameters['csv_path'], 'participants.csv'))
contracts.iloc[start_index:].to_csv(os.path.join(parameters['csv_path'],'contracts.csv'))
print("Saving to CSVS")
print("=========================")


try:
    cursor = connection.connect_db().cursor()
except Exception as e:
    print(e)
    print("Database connection failed!")
else:
    print("Database connection successful!")
    batch_size = 1000
    save_data_into_db(cursor, os.path.join(parameters['csv_path'], 'contracts.csv'), ia_db.save_contract_history,
                      batch_size)
    if control_unit == 1:
        save_data_into_db(cursor, os.path.join(parameters['csv_path'],'savings.csv'), ia_db.save_saving_history, batch_size)
        save_data_into_db(cursor, os.path.join(parameters['csv_path'],'funds.csv'), ia_db.save_fund_history, batch_size)
    elif control_unit == 2:
        save_data_into_db(cursor, os.path.join(parameters['csv_path'], 'transactions.csv'),
                          ia_db.save_transaction_history, batch_size)
    else:
        save_data_into_db(cursor, os.path.join(parameters['csv_path'], 'participants.csv'),
                          ia_db.save_participant_history, batch_size)
        save_data_into_db(cursor, os.path.join(parameters['csv_path'], 'beneficiaries.csv'),
                          ia_db.save_beneficiary_history, batch_size)
        save_data_into_db(cursor, os.path.join(parameters['csv_path'], 'clients.csv'), ia_db.save_client_history,
                          batch_size)

print("Saving to Databases")
print("=========================")

