from datetime import datetime
from time import sleep
import pandas as pd

from selenium.webdriver.common.by import By

from eq_selenium import eq_scrap
from dbutilities import dbColumns
from eq_selenium.eq_scrap import login
from utilities.companys import companies
from utilities.get_confs import get_confs
from utilities.web_driver import driver_setup
from utilities import get_account

# scraping for investment
confs = get_confs(companies['EQ'])
wd = login(confs)
wd.get(confs['parameters']['index_url'] + '600658785')
statement_date = datetime.today().strftime('%Y-%m-%d')
text = wd.find_element(By.XPATH, '//*[@id="policy_content"]/div[1]/h1[1]').text.split(' (', 1)
policy_number = text[1][:-1]
investment_type = text[0]
account_type = wd.find_element(By.XPATH, '//*[@id="policy_content"]/div[3]/div[1]/p[2]/span').text
result = [statement_date, policy_number, account_type, investment_type]

print(result)

# determine if table exist
elements = wd.find_elements(By.XPATH, '//*[@id="policy_details"]/div[3]/div/div[3]/div[1]/*')
row_data = []
for element in elements:
    if elements[2].tag_name != 'table':
        category = 'TERMINATED'
        result.append(category)
        row_data.append([None]*6)

    else:
        # TODO finish and test code
        category = None








# extract row data from table


