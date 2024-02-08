from time import sleep
import pandas as pd

from selenium.webdriver.common.by import By

from cl_selenium import cl_scrap, cl_selectors, cl_transactions, cl_holdings
from dbutilities import dbColumns

# save cl_conf as parameters
parameters = cl_scrap.cl_account()

# set up Chrome driver
wd = cl_scrap.driver_setup(parameters)
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
sleep(5)

# transactions = pd.DataFrame(columns=dbColumns.transaction_columns)
# test_transactions = cl_transactions.scrape_transactions(wd, transactions)
# print(test_transactions)

holdings = pd.DataFrame(columns=["Category", "Fund_code", "Fund_name", "Units", "Unit_value", "Value", "ACB"])
test_holdings = cl_holdings.scrape_holdings(wd, holdings)
print(test_holdings)

# wd.find_element(By.XPATH, paths['holdings']).click()
# sleep(5)

