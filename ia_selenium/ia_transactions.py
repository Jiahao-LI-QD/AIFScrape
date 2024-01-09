import time

from selenium.webdriver.common.by import By
from ia_selenium import ia_selectors


def scrape_transaction(wd, transaction, issue_date):
    paths = ia_selectors.transactions_path()
    wd.find_element(By.XPATH, paths['transaction_button']).click()

    ## TODO#1: best to change to 'page is finished loading'
    time.sleep(10)
    wd.find_element(By.XPATH, paths['issue_date']).clear()
    wd.find_element(By.XPATH, paths['issue_date']).send_keys(issue_date)
    wd.find_element(By.XPATH, paths['refresh_Button']).click()

    # grab contract number and keep only the 10 digits between ' - '
    text = wd.find_element(By.XPATH, paths['contract_number_account_type']).text
    contract_number = text.split(' - ')[1]

    # grab contents of the transaction table
    row = wd.find_elements(By.XPATH, paths['row_data'])
    for cell in row:
        Date = cell.find_element(By.XPATH, './td[1]').text
        Transaction = cell.find_element(By.XPATH, './td[2]').text
        Fund = cell.find_element(By.XPATH, './td[3]').text
        Gross_Amount = cell.find_element(By.XPATH, './td[4]').text
        Units = cell.find_element(By.XPATH, './td[5]').text.replace(',', '')
        Unit_Value = cell.find_element(By.XPATH, './td[6]').text.replace(',', '')
        transaction.loc[len(transaction)] = [contract_number, Date, Transaction, Fund, Gross_Amount, Units,
                                             Unit_Value]

    # for "Next" button when there is more than one page of transactions
    while wd.find_element(By.XPATH, paths['next_page']) and 'Next' in wd.find_element(By.XPATH, paths["next_page"]).get_attribute("outerHTML"):
        wd.find_element(By.XPATH, paths['next_page']).click()
        # <span align="right">Next</span> outerHTML
        # wd.find_element(By.XPATH, paths['next_page']):
        #         wd.find_element(By.XPATH, paths['next_page']).click()

        time.sleep(20)

        row = wd.find_elements(By.XPATH, paths['row_data'])
        for cell in row:
            Date = cell.find_element(By.XPATH, './td[1]').text
            Transaction = cell.find_element(By.XPATH, './td[2]').text
            Fund = cell.find_element(By.XPATH, './td[3]').text
            Gross_Amount = cell.find_element(By.XPATH, './td[4]').text
            Units = cell.find_element(By.XPATH, './td[5]').text
            Unit_Value = cell.find_element(By.XPATH, './td[6]').text
            transaction.loc[len(transaction)] = [contract_number, Date, Transaction, Fund, Gross_Amount, Units,
                                                 Unit_Value]




## 2nd page XPath: //*[@id="TransactionsTrouveesDiv"]/div[3]/table/tbody/tr[9]/td[4]
