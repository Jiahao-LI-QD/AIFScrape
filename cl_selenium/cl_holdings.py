from time import sleep
from locale import atof
from datetime import datetime
from collections import OrderedDict

import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from cl_selenium import cl_selectors
from utilities.companys import companies


def scrape_holdings(wd, holdings):
    """
    This method scrape holding table by taking a WebDriver object and a DataFrame as inputs,
    and returns the updated DataFrame.

    :param wd:chrome webdriver
    :param holdings:holdings dataframe to store the scraped data.
    :return:The updated DataFrame with the scraped transaction data.

    Workflow:
    - On 'Summary' page:
    1.Extract  statement date and format it to 'YYYY-MM-DD' format.
    2.Get the contract number and guarantee(part of investment type)
    3.Extract the account type and investment type from the text on the web page.
    4.Append the formatted date, contract number, account type, and investment type to the result list.
    - Click on the 'Holdings' page:
    1.Find the table element on the web page.
    2.Iterate over each row in the table.
    3.Check if the row is a category row or a data row.
    4.If it is a category row, update the category variable.
    5.If it is a data row, extract the data from each column and append it to the row_data list.
    6. Append the result list, row_data list, and the company name as the final list to the holdings DataFrame.
    7.If row_data under same category, assign row_data = [category]
    8.Repeat steps 1-8 for each row in the table.
    9. Return the updated holdings DataFrame.
    """
    # defining variable category as an empty string
    category = ''
    # calling holding xpath from cl_selector
    paths = cl_selectors.holdings_paths()
    # extracting data from 'summary' page
    statement_date = wd.find_element(By.XPATH, paths['statement_date']).text
    formatted_date = datetime.strptime(statement_date, '%b. %d, %Y').strftime('%Y-%m-%d')
    contract_number = wd.find_element(By.XPATH, paths['contract_number']).text
    guarantee = wd.find_element(By.XPATH, paths['guarantee']).text
    text = wd.find_element(By.XPATH, paths['text']).text.split(' (', 1)
    account_type = text[0]
    investment_type = text[1][:-1] + guarantee
    result = [formatted_date, contract_number, account_type, investment_type]
    sleep(1)
    # extracting table data from 'holdings' page
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
            # initiating first element in row_data to category
            if len(row_data) == 0:
                row_data.append(category)
            else:
                row_data[0] = category

        else:
            for column in columns:
                # appending column data to row_data
                row_data.append(column.text)
            # assigning 'None' to 'ACB' column
            row_data.append(None)
            final = result + row_data
            final.append(companies['CL'])
            holdings.loc[len(holdings)] = final
            # for column data under same category:
            row_data = [category]

    return holdings
