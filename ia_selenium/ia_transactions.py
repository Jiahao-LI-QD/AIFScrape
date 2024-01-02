import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from ia_selenium import ia_login
from selenium.webdriver.support.wait import WebDriverWait

wd = webdriver.Chrome()

wd.implicitly_wait(20)

wd.get(ia_conf.web_url)

ia_login.login(wd)

# TODO#0: read csv to find contract number

wd.find_element(By.XPATH, '//*[@id="ContractNumber"]').send_keys('1819806281')

wd.find_element(By.XPATH, '//*[@id="btnSearch"]').click()

## going to the transactions page
wd.find_element(By.XPATH, '//*[@id="Transactions"]').click()

## TODO#1: find date from downloaded excel or contract specification

## TODO#2: best to change to 'page is finished loading'
def scrape_transactions(wd, transactions):
    time.sleep(5)
    wd.find_element(By.XPATH, '//*[@id="Debut"]').clear()
    wd.find_element(By.XPATH, '//*[@id="Debut"]').send_keys('2023-03-01')
    wd.find_element(By.XPATH, '//*[@id="rechercheTransactions"]').click()

    transactions = []

## TODO#3: grab contract number and keep only the 10 digits between ' - '

    data = wd.find_element(By.XPATH, '//*[@id="TransactionsTrouveesDiv"]/div[3]/table/tbody').text
    transactions.append(data)

    print(data)
    print(transactions)

input()
# //*[@id="TransactionsTrouveesDiv"]/div[3]/table/thead/tr/th[1]
# //*[@id="TransactionsTrouveesDiv"]/div[3]/table/thead/tr/th[2]
# //*[@id="TransactionsTrouveesDiv"]/div[3]/table/thead/tr/th[6]
#
# //*[@id="TransactionsTrouveesDiv"]/div[3]/table/tbody/tr[1]/td[1]
# //*[@id="TransactionsTrouveesDiv"]/div[3]/table/tbody/tr[1]/td[2]
# //*[@id="TransactionsTrouveesDiv"]/div[3]/table/tbody/tr[1]/td[3]
# //*[@id="TransactionsTrouveesDiv"]/div[3]/table/tbody/tr[9]/td[4]

# Date	Transaction	Fund	Gross amount	Units	Unit value
# 2023-11-30	Interest	HISA 	$26.36
# 2023-10-31	Interest	HISA 	$27.13
# 2023-09-30	Interest	HISA 	$26.16
# 2023-08-31	Interest	HISA 	$26.93
# 2023-07-31	Interest	HISA 	$26.83
# 2023-06-30	Interest	HISA 	$25.08
# 2023-05-31	Interest	HISA 	$25.18
# 2023-04-30	Interest	HISA 	$24.54
# 2023-03-31	Interest	HISA 	$24.73
# 2023-03-01	Premium	HISA 	$7,000.00
## Notes for TODO #2
# elements = wait.until(
#   EC.element_to_be_clickable((By.XPATH, "***"))
# ).find_elements(By.XPATH, "***")