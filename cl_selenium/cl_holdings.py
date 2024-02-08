import time
from locale import atof
from datetime import datetime
from collections import OrderedDict

import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from cl_selenium import cl_selectors

def scrape_holdings(wd, holdings):
    global category
    paths = cl_selectors.holdings_paths()
    wd.find_element(By.XPATH, paths['holdings_button']).click()

    # loading table data
    table_element = wd.find_elements(By.XPATH, paths['table_xpath'])
    row_data = []

    for row in table_element[0].find_elements(By.XPATH, ".//tr"):

        # determining if the row is a category row or data row
        if row.find_elements(By.XPATH, ".//th"):
            category = row.text
            if len(row_data) == 0:
                row_data.append(category)
            else:
                row_data[0] = category

        else:
            columns = row.find_elements(By.XPATH, ".//td")
            for column in columns:
                row_data.append(column.text)
            row_data.append(None)
            holdings.loc[len(holdings)] = row_data
            row_data = [category]