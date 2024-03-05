import time
from datetime import datetime
from collections import OrderedDict

from selenium.webdriver.common.by import By
from cl_selenium import cl_selectors
from utilities.companys import companies


def scrape_transactions(wd, transactions):
    """
    scrape transaction data by taking a WebDriver object and a DataFrame as inputs, and returns the updated DataFrame.
    :param wd: chrome webdriver
    :param transactions: transactions dataframe to store the scraped data.
    :return: The updated DataFrame with the scraped transaction data.

    1. Obtain XPath paths for elements and navigate to summary and transactions pages.
    2. Convert issue date format and enter start & end dates, Apply changes.
    3. Extract contract number.
    4. Iterate over table rows and store cell text in a list.
    5. Remove duplicate values in the list due to unique table structure.
    6. Create new row with contract number and unique data and append to transactions DataFrame.
    7. Return updated transactions DataFrame.
    """

    paths = cl_selectors.transaction_paths()

    # find the issue date from summary page, check if the account is too new/empty.
    wd.find_element(By.XPATH, paths['summary_button']).click()
    if len(wd.find_elements(By.XPATH, paths['issue_date'])) == 0:
        return

    input_date_string = wd.find_element(By.XPATH, paths['issue_date']).text

    # going to transactions page
    wd.find_element(By.XPATH, paths['Transactions_button']).click()
    time.sleep(1)

    # change the issue date to the right format
    input_format = '%b. %d, %Y'
    output_format = '%B %d, %Y'
    try:
        parsed_date = datetime.strptime(input_date_string, input_format)
        start_date = parsed_date.strftime(output_format)
    except ValueError:
        start_date = input_date_string

    # input dates and apply changes
    wd.find_element(By.XPATH, paths['start_date']).send_keys(start_date)
    date_today = datetime.today().date()
    end_date = date_today.strftime("%B %d, %Y")
    wd.find_element(By.XPATH, paths['end_date']).send_keys(end_date)
    wd.find_element(By.XPATH, paths['date_apply']).click()

    # Scrap contract number and keep only the 10 digits between ' - '
    text = wd.find_element(By.XPATH, paths['contract_number']).text
    contract_number = text

    table = wd.find_elements(By.XPATH, paths['table_body'])
    for row in table:
        rows = row.find_elements(By.XPATH, ".//*")
        result = [cell.text for cell in rows]
        unique_list = list(OrderedDict.fromkeys(result))

        new_row = [contract_number]
        new_row.extend(unique_list[:6])
        new_row[-2] = new_row[-2].replace("$", "")
        new_row[-2] = float(new_row[-2].replace(",", ""))
        new_row[2], new_row[3], new_row[4], new_row[5], new_row[6] = new_row[3], new_row[2], new_row[6], new_row[4], new_row[5]
        new_row.append(companies['CL'])
        transactions.loc[len(transactions)] = new_row
