import sys
import os
from datetime import datetime

from cl_scrap import wd
from selenium import webdriver
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

from cl_selenium import cl_selectors

from cl_scrap import cl_account, driver_setup, login
paths = cl_selectors.fund_paths()
statement_date = wd.find_element(By.XPATH, paths['statement_date']).text
formatted_date = datetime.strptime(statement_date, '%b. %d, %Y').strftime('%Y-%m-%d')
contract_number = wd.find_element(By. XPATH, paths['contract_number']).text
holdings = wd.find_element(By.XPATH, paths['holdings_button']).click
text = wd.find_element(By.XPATH, paths['text']).text.split(' (', 1)
account_type = text[0]
investment_type = text[1][:-1]



