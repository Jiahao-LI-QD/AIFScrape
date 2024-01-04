import ia_scrap
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from ia_selenium import ia_login, ia_transactions
from dbutilities import dbColumns
import pandas as pd
from ia_selenium import keys
from selenium.webdriver.support import expected_conditions as EC

# required parameters for app
try:
    parameters = keys.ia_account()
except Exception as e:
    print(e)
    exit()

# start web driver
wd = webdriver.Chrome()

wd.implicitly_wait(15)

wd.get(parameters['web_url'])

ia_login.login(wd, parameters['username'], parameters['password'])
# accept cookie
# accept cookie
wait = WebDriverWait(wd, 10)  # seconds want to wait
wait.until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/a[1]"))
).click()

# create pointers
client = pd.DataFrame(columns=dbColumns.client_columns)
saving = pd.DataFrame(columns=dbColumns.saving_columns)
beneficiary = pd.DataFrame(columns=dbColumns.beneficiary_columns)
participant = pd.DataFrame(columns=dbColumns.participant_columns)
transaction = pd.DataFrame(columns=dbColumns.transaction_columns)
fund = pd.DataFrame(columns=dbColumns.fund_columns)

wd.find_element(By.XPATH, '//*[@id="mnMesClients"]/a').click()
wd.find_element(By.XPATH, '//*[@id="ContractNumber"]').clear()
wd.find_element(By.XPATH, '//*[@id="ContractNumber"]').send_keys(ia_scrap.row['Contract_number'])
wd.find_element(By.XPATH, '//*[@id="btnSearch"]').click()

ia_transactions.scrape_transaction(wd, transaction)

print(len(transaction))
print(transaction)


# import os.path
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
#
# from ia_selenium import ia_login, ia_investment
# from dbutilities import dbColumns
# import pandas as pd
# from ia_selenium import keys
# from selenium.webdriver.support import expected_conditions as EC
#
# # required parameters for app
# try:
#     parameters = keys.ia_account()
# except Exception as e:
#     print(e)
#     exit()
#
# # start web driver
# wd = webdriver.Chrome()
#
# wd.implicitly_wait(15)
#
# wd.get(parameters['web_url'])
#
# ia_login.login(wd, parameters['username'], parameters['password'])
# # accept cookie
# wait = WebDriverWait(wd, 10)  # seconds want to wait
# wait.until(
#     EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/a[1]"))
# ).click()
#
# # TODO#0: read csv to find contract number
# wd.find_element(By.XPATH, '//*[@id="mnMesClients"]').click()
# wd.find_element(By.XPATH, '//*[@id="ContractNumber"]').send_keys('1819806281')
# wd.find_element(By.XPATH, '//*[@id="btnSearch"]').click()
#
# ## going to the transactions page
# wd.find_element(By.XPATH, '//*[@id="Transactions"]').click()
#
# ## TODO#1: find date from downloaded excel or contract specification
#
# ## TODO#2: best to change to 'page is finished loading'
# time.sleep(5)
# wd.find_element(By.XPATH, '//*[@id="Debut"]').clear()
# wd.find_element(By.XPATH, '//*[@id="Debut"]').send_keys('2023-03-01')
# wd.find_element(By.XPATH, '//*[@id="rechercheTransactions"]').click()
#
# transactions = pd.DataFrame(columns=dbColumns.transaction_columns)
#
# # grab contract number and keep only the 10 digits between ' - '
# text = wd.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[1]/div/span').text
# contract_number = text.split(' - ')[1]
#
# # grab contents of the transaction table
# table = wd.find_elements(By.XPATH, '//*[@id="TransactionsTrouveesDiv"]/div[3]/table/tbody/tr')
# for transaction in table:
#     Date = transaction.find_element(By.XPATH, './td[1]').text
#     Transaction = transaction.find_element(By.XPATH, './td[2]').text
#     Fund = transaction.find_element(By.XPATH, './td[3]').text
#     Gross_Amount = transaction.find_element(By.XPATH, './td[4]').text
#     Units = transaction.find_element(By.XPATH, './td[5]').text
#     Unit_Value = transaction.find_element(By.XPATH, './td[6]').text
#     transactions.loc[len(transactions)] = [contract_number, Date, Transaction, Fund, Gross_Amount, Units, Unit_Value]
#
# print(contract_number)
# print(transactions)
#
# input()
# # //*[@id="TransactionsTrouveesDiv"]/div[3]/table/tbody/tr[1]/td[1]
# # //*[@id="TransactionsTrouveesDiv"]/div[3]/table/tbody/tr[1]/td[2]
# # //*[@id="TransactionsTrouveesDiv"]/div[3]/table/tbody/tr[1]/td[3]
# # //*[@id="TransactionsTrouveesDiv"]/div[3]/table/tbody/tr[9]/td[4]
#
# # Date	Transaction	Fund	Gross amount	Units	Unit value
# # 2023-11-30	Interest	HISA 	$26.36
# # 2023-10-31	Interest	HISA 	$27.13
# # 2023-09-30	Interest	HISA 	$26.16
# # 2023-08-31	Interest	HISA 	$26.93
# # 2023-07-31	Interest	HISA 	$26.83
# # 2023-06-30	Interest	HISA 	$25.08
# # 2023-05-31	Interest	HISA 	$25.18
# # 2023-04-30	Interest	HISA 	$24.54
# # 2023-03-31	Interest	HISA 	$24.73
# # 2023-03-01	Premium	HISA 	$7,000.00