from time import sleep
import pandas as pd

from selenium.webdriver.common.by import By

from cl_selenium import cl_scrap, cl_selectors, cl_transactions

# save cl_conf as parameters
parameters = cl_scrap.cl_account()
print(parameters)

# set up Chrome driver
wd = cl_scrap.driver_setup(parameters)
wd.get(parameters['web_url'])

# testing for log in function
cl_scrap.login(wd, parameters['username'], parameters['password'])

# Going to an account for testing
traverse_paths = cl_selectors.traverse_paths()
wd.find_element(By.XPATH, traverse_paths['search_field']).send_keys(410351753)
sleep(1)
wd.find_element(By.XPATH, traverse_paths['search_button']).click()
sleep(5)

# testing for transactions page
transaction_paths = cl_selectors.transaction_paths()
issue_date = wd.find_element(By.XPATH, transaction_paths['issue_date']).text
print(issue_date)

transactions = pd.DataFrame()
test_table = cl_transactions.scrape_transaction(wd, transactions, issue_date)
print(transactions)
# TODO: Eva's code here

# wd.find_element(By.XPATH, paths['holdings']).click()
# sleep(5)

# TODO: Christina's code here
