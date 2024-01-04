import os.path
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from ia_selenium import ia_login, ia_investment, ia_transactions, ia_client
from dbutilities import dbColumns
import pandas as pd
from ia_selenium import keys
from selenium.webdriver.support import expected_conditions as EC

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
# accept cookie
# accept cookie
time.sleep(1)
wait = WebDriverWait(wd, 10)  # seconds want to wait
wait.until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/a[1]"))
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

    wd.find_element(By.XPATH, '//*[@id="mnMesClients"]/a').click()

    wd.find_element(By.XPATH, '//*[@id="ContractNumber"]').clear()

    wd.find_element(By.XPATH, '//*[@id="ContractNumber"]').send_keys(row['Contract_number'])

    wd.find_element(By.XPATH, '//*[@id="btnSearch"]').click()

    # TODO: Control Unit
    ia_investment.scrape_investment(wd, fund, saving)

    ia_transactions.scrape_transaction(wd, transaction, row['Contract_start_date'])

    ia_client.scrape(wd, client, beneficiary, participant)

fund.to_csv(os.path.join(parameters['csv_path'],'funds.csv'))
saving.to_csv(os.path.join(parameters['csv_path'],'savings.csv'))
transaction.to_csv(os.path.join(parameters['csv_path'],'transactions.csv'))
client.to_csv(os.path.join(parameters['csv_path'],'clients.csv'))
beneficiary.to_csv(os.path.join(parameters['csv_path'],'beneficiaries.csv'))
participant.to_csv(os.path.join(parameters['csv_path'],'participants.csv'))

