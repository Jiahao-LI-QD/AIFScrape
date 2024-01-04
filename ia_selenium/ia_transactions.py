import time
from selenium.webdriver.common.by import By

def scrape_transaction(wd, transaction):
    wd.find_element(By.XPATH, '//*[@id="Transactions"]').click()

    ## TODO#1: find date from downloaded excel or contract specification

    ## TODO#2: best to change to 'page is finished loading'
    time.sleep(10)
    wd.find_element(By.XPATH, '//*[@id="Debut"]').clear()
    wd.find_element(By.XPATH, '//*[@id="Debut"]').send_keys('2023-03-01')
    wd.find_element(By.XPATH, '//*[@id="rechercheTransactions"]').click()

    # grab contract number and keep only the 10 digits between ' - '
    text = wd.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[1]/div/span').text
    contract_number = text.split(' - ')[1]

    # grab contents of the transaction table
    row = wd.find_elements(By.XPATH, '//*[@id="TransactionsTrouveesDiv"]/div[3]/table/tbody/tr')
    for cell in row:
        Date = cell.find_element(By.XPATH, './td[1]').text
        Transaction = cell.find_element(By.XPATH, './td[2]').text
        Fund = cell.find_element(By.XPATH, './td[3]').text
        Gross_Amount = cell.find_element(By.XPATH, './td[4]').text
        Units = cell.find_element(By.XPATH, './td[5]').text
        Unit_Value = cell.find_element(By.XPATH, './td[6]').text
        transaction.loc[len(transaction)] = [contract_number, Date, Transaction, Fund, Gross_Amount, Units,
                                               Unit_Value]
    print(transaction)