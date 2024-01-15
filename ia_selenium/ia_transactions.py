import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ia_selenium import ia_selectors


def scrape_transaction(wd, transaction, issue_date):
    paths = ia_selectors.transactions_path()
    wd.find_element(By.XPATH, paths['transaction_button']).click()

    # Wait until the entire page finishes loading
    wait = WebDriverWait(wd, 40)
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
    row = wd.find_elements(By.XPATH, paths['row_data'])
    for cell in row:
        cells = cell.find_elements(By.XPATH, ".//*")
        result = [b.text for b in cells]
        transaction.loc[len(transaction)] = [contract_number].extend(result)

    # for "Next" button when there is more than one page of transactions
    while len(wd.find_elements(By.XPATH, paths['next_page'])) > 0:
        next_page_button = wd.find_element(By.XPATH, paths['next_page'])
        if 'Next' not in next_page_button.get_attribute("outerHTML"):
            break
        print('There is another page of transactions')
        next_page_button.click()

        # Wait until the entire page finishes loading
        wait = WebDriverWait(wd, 40)
        wait.until(EC.visibility_of_element_located((By.XPATH, paths['table_header'])))
        time.sleep(1)

        row = wd.find_elements(By.XPATH, paths['row_data'])
        for cell in row:
            cells = cell.find_elements(By.XPATH, ".//*")
            result = [b.text for b in cells]
            transaction.loc[len(transaction)] = [contract_number].extend(result)

        # row = wd.find_elements(By.XPATH, paths['row_data'])
        # for cell in row:
        #     Date = cell.find_element(By.XPATH, './td[1]').text
        #     Transaction = cell.find_element(By.XPATH, './td[2]').text
        #     Fund = cell.find_element(By.XPATH, './td[3]').text
        #     Gross_Amount = cell.find_element(By.XPATH, './td[4]').text
        #     Units = cell.find_element(By.XPATH, './td[5]').text
        #     Unit_Value = cell.find_element(By.XPATH, './td[6]').text
        #     transaction.loc[len(transaction)] = [contract_number, Date, Transaction, Fund, Gross_Amount, Units,
        #                                          Unit_Value]

