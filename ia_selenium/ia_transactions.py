import time
from locale import atof

import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ia_selenium import ia_selectors


def scrape_transaction(wd, transaction, issue_date):
    paths = ia_selectors.transactions_path()
    wd.find_element(By.XPATH, paths['transaction_button']).click()

    # Wait until the entire page finishes loading
    wait = WebDriverWait(wd, 30)
    wait.until(EC.visibility_of_element_located((By.XPATH, paths['table_header'])))
    time.sleep(1)

    # Inputting "From" date
    wd.find_element(By.XPATH, paths['issue_date']).clear()
    wd.find_element(By.XPATH, paths['issue_date']).send_keys(issue_date)
    wd.find_element(By.XPATH, paths['refresh_Button']).click()

    # Scrap contract number and keep only the 10 digits between ' - '
    text = wd.find_element(By.XPATH, paths['contract_number_account_type']).text
    contract_number = text.split(' - ')[1]

    # grab contents of the transaction table
    table = wd.find_elements(By.XPATH, paths['table_data'])

    for row in table:
        rows = row.find_elements(By.XPATH, ".//*")
        result = [cell.text for cell in rows]

        new_row = [contract_number]
        new_row.extend(result)
        new_row[-1] = atof(new_row[-1].replace(',', ''))
        new_row[-2] = atof(new_row[-2].replace(',', ''))
        transaction.loc[len(transaction)] = new_row

    # for "Next" button when there is more than one page of transactions
    while len(wd.find_elements(By.CSS_SELECTOR, paths['CSS_next_page'])) > 0:
        next_page_button = wd.find_element(By.CSS_SELECTOR, paths['CSS_next_page'])
        print('There is another page of transactions')
        next_page_button.click()

        # Wait until the entire page finishes loading
        wait = WebDriverWait(wd, 30)
        wait.until(EC.visibility_of_element_located((By.XPATH, paths['table_header'])))
        time.sleep(1)

        table = wd.find_elements(By.XPATH, paths['table_data'])
        for row in table:
            rows = row.find_elements(By.XPATH, ".//*")
            result = [cell.text for cell in rows]

            entire_row = [contract_number]
            entire_row.extend(result)
            entire_row[-1] = atof(entire_row[-1].replace(',', ''))
            entire_row[-2] = atof(entire_row[-2].replace(',', ''))
            transaction.loc[len(transaction)] = entire_row

