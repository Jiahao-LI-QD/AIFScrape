from time import sleep
from locale import atof
from datetime import datetime
from collections import OrderedDict

import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from cl_selenium import cl_selectors

def scrape_holdings(wd, holdings):
    category = ''
    paths = cl_selectors.holdings_paths()
    statement_date = wd.find_element(By.XPATH, paths['statement_date']).text
    formatted_date = datetime.strptime(statement_date, '%b. %d, %Y').strftime('%Y-%m-%d')
    contract_number = wd.find_element(By.XPATH, paths['contract_number']).text
    sleep(1)
    wd.find_element(By.XPATH, paths['holdings_button']).click()
    text = wd.find_element(By.XPATH, paths['text']).text.split(' (', 1)
    account_type = text[0]
    investment_type = text[1][:-1]
    result = [formatted_date, contract_number, account_type, investment_type]
    wd.find_element(By.XPATH, paths['holdings_button']).click()

    # loading table data
    table_element = wd.find_elements(By.XPATH, paths['table_xpath'])
    row_data = []
    rows = table_element[0].find_elements(By.XPATH, "./tr")
    for row in rows:


        # determining if the row is a category row or data row
        columns = row.find_elements(By.XPATH, "./*")
        if columns and columns[0].tag_name == 'th':
            category = row.text
            if len(row_data) == 0:
                row_data.append(category)
            else:
                row_data[0] = category

        else:
            for column in columns:
                row_data.append(column.text)
            row_data.append(None)
            final = result + row_data
            final.append('CL')
            holdings.loc[len(holdings)] = final
            row_data = [category]

    return holdings
