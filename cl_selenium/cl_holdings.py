from time import sleep
from locale import atof
from datetime import datetime
from collections import OrderedDict

import pandas as pd
from selenium.webdriver import ActionChains
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
    try:
        # Try parsing the statement date with the first format '%b. %d, %Y'
        formatted_date = datetime.strptime(statement_date, '%b. %d, %Y')
    except ValueError:
        try:
            # Try parsing the statement date with the second format '%B. %d, %Y'
            formatted_date = datetime.strptime(statement_date, '%B %d, %Y')
        except ValueError:
            # If the statement date doesn't match either format, keep it as it is
            formatted_date = None

    # If the statement date matched one of the formats, convert it to '%Y-%m-%d'
    if formatted_date:
        formatted_date_str = formatted_date.strftime('%Y-%m-%d')
    else:
        # Otherwise, keep the statement date unchanged
        formatted_date_str = statement_date
    contract_number = wd.find_element(By.XPATH, paths['contract_number']).text
    # guarantee = wd.find_element(By.XPATH, paths['guarantee']).text
    text = wd.find_element(By.XPATH, paths['text']).text.split(' (', 1)
    # investment_type = text[0] + ' ' + guarantee
    account_type = text[1][:-1]

    if len(wd.find_elements(By.XPATH, paths['guarantee'])) != 0:
        guarantee_row = wd.find_element(By.XPATH, paths['guarantee']).text
    else:
        guarantee_row = ''

    investment_type = text[0] + guarantee_row
    result = [formatted_date_str, contract_number, account_type, investment_type]
    # extracting table data from 'holdings' page
    if len(wd.find_elements(By.XPATH, paths['holdings_button'])) == 0:
        result.extend([None]*7)
        result.append('CL')
        result[0] = datetime.today().strftime('%Y-%m-%d')
        holdings.loc[len(holdings)] = result

    else:
        holdings_button = wd.find_element(By.XPATH, paths['holdings_button'])
        # Perform the click action using ActionChains
        actions = ActionChains(wd)
        actions.click(holdings_button).perform()
        sleep(1)

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
                    if column.text == '--':
                        row_data.extend([None])
                    else:
                        row_data.append(column.text)
                # assigning 'None' to 'ACB' column
                row_data.append(None)
                final = result + row_data
                if final[8] != None:
                    final[8] = float(final[8].replace("$", ""))
                else:
                    final.insert(4, None)
                if final[-4] != None:
                    final[-4] = float(final[-4].replace(",", ""))
                final.append(companies['CL'])
                holdings.loc[len(holdings)] = final
                # for column data under same category:
                row_data = [category]