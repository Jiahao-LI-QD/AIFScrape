from time import sleep
import pandas as pd

from selenium.webdriver.common.by import By

from cl_selenium import cl_scrap, cl_selectors, cl_transactions, cl_holdings, cl_client, cl_participant, cl_beneficiary
from dbutilities import dbColumns
from utilities.web_driver import driver_setup

# save cl_conf as parameters
parameters = cl_scrap.cl_account()

# set up Chrome driver
wd = driver_setup(parameters)
wd.get(parameters['web_url'])
sleep(1)

# testing for log in function
cl_scrap.login(wd, parameters['username'], parameters['password'])

# Going to an account for testing
traverse_paths = cl_selectors.traverse_paths()
sleep(1)
wd.find_element(By.XPATH, traverse_paths['search_field']).send_keys(310127600)
sleep(2)
wd.find_element(By.XPATH, traverse_paths['search_button']).click()
sleep(10)


client=pd.DataFrame(columns=dbColumns.client_columns)
test_client=cl_client.scrape_client(wd,client)
print(test_client)

participant=pd.DataFrame(columns=dbColumns.participant_columns)
test_participant= cl_participant.scrape_participant(wd,participant)
print(test_participant)

beneficiary=pd.DataFrame(columns=dbColumns.beneficiary_columns)
test_beneficiary=cl_beneficiary.scrape_beneficiary(wd,beneficiary)
print(test_beneficiary)

sleep(5)

holdings = pd.DataFrame(columns=dbColumns.fund_columns)
test_holdings = cl_holdings.scrape_holdings(wd, holdings)
print(test_holdings)

transactions = pd.DataFrame(columns=dbColumns.transaction_columns)
test_transactions = cl_transactions.scrape_transactions(wd, transactions)
print(test_transactions)
# pd.set_option('display.max_columns', None)
# print(test_holdings.head())
# wd.find_element(By.XPATH, paths['holdings']).click()
# sleep(5)

