import time
from locale import atof
from datetime import datetime
from collections import OrderedDict

import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from cl_selenium import cl_selectors


def scrape_transactions(wd, transactions):
    paths = cl_selectors.transaction_paths()

    # find the issue date from summary page
    wd.find_element(By.XPATH, paths['summary_button']).click()
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
        new_row.extend(unique_list)
        new_row.pop()
        transactions.loc[len(transactions)] = new_row

    return transactions

    # If transaction is empty.
    # has_transaction = wd.find_element(By.XPATH, paths['has_transaction']).text
    # if 'transactions' not in has_transaction:
    #     # grab contents of the transaction table
    #     table = wd.find_elements(By.XPATH, paths['table_data'])
    #     for row in table:
    #         rows = row.find_elements(By.XPATH, ".//*")
    #         result = [cell.text for cell in rows]
    #
    #         new_row = [contract_number]
    #         new_row.extend(result)
    #         if new_row[-2] != "":
    #             new_row[-1] = atof(new_row[-1].replace(',', ''))
    #             new_row[-2] = atof(new_row[-2].replace(',', ''))
    #         elif len(new_row) == 8:
    #             new_row.pop(4)
    #         transaction.loc[len(transaction)] = new_row
    #
    #     # for "Next" button when there is more than one page of transactions
    #     while len(wd.find_elements(By.CSS_SELECTOR, paths['CSS_next_page'])) > 0:
    #         next_page_button = wd.find_element(By.CSS_SELECTOR, paths['CSS_next_page'])
    #         next_page_button.click()
    #
    #         # Wait until the entire page finishes loading
    #         wait = WebDriverWait(wd, 30)
    #         wait.until(EC.visibility_of_element_located((By.XPATH, paths['table_header'])))
    #         time.sleep(1)
    #
    #         table = wd.find_elements(By.XPATH, paths['table_data'])
    #         for row in table:
    #             rows = row.find_elements(By.XPATH, ".//*")
    #             result = [cell.text for cell in rows]
    #
    #             entire_row = [contract_number]
    #             entire_row.extend(result)
    #             if entire_row[-2] != "":
    #                 entire_row[-1] = atof(entire_row[-1].replace(',', ''))
    #                 entire_row[-2] = atof(entire_row[-2].replace(',', ''))
    #             elif len(entire_row) == 8:
    #                 entire_row.pop(4)
    #             transaction.loc[len(transaction)] = entire_row
    #
    #     wd.execute_script("window.scrollTo(0, 0)")
