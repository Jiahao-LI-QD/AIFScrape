from selenium import webdriver
from selenium.webdriver.common.by import By
from ia_selenium import keys

wd = webdriver.Chrome()

wd.implicitly_wait(15)

wd.get('https://iaa.secureweb.inalco.com/MKMWPN23/home')

# click login
wd.find_element(By.XPATH, '//*[@id="eeCleanLoader"]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div[1]/a').click()

wd.find_element(By.XPATH, '//*[@id="idp-discovery-username"]').send_keys(keys.ia_account()["user"])
#
# input()
wd.find_element(By.XPATH, '/html/body/div[2]/div[2]/a[1]').click()

wd.find_element(By.XPATH, '//*[@id="idp-discovery-submit"]').click()

wd.find_element(By.XPATH, '//*[@id="okta-signin-password"]').send_keys(keys.ia_account()["pwd"])

wd.find_element(By.XPATH, '//*[@id="okta-signin-submit"]').click()

wd.find_element(By.XPATH, '//*[@id="mnMesClients"]/a').click()

# TODO read csv to find contract number

wd.find_element(By.XPATH, '//*[@id="ContractNumber"]').send_keys('1819806281')

wd.find_element(By.XPATH, '//*[@id="btnSearch"]').click()

wd.find_element(By.XPATH,'//*[@id="Placements"]').click()
type = wd.find_element(By.XPATH,'//*[@id="content"]/div[4]/div[1]/div/div[1]').text

Statement_Date = wd.find_element(By.XPATH, '//*[@id="content"]/div[3]').text
Contract_number = wd.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[1]/div/span').text
Account_type = wd.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[1]/div/span').text
Investment_type = wd.find_element(By.XPATH, '//*[@id="content"]/div[4]/div[1]/div/div[1]').text
Rate = wd.find_element(By.XPATH, '//*[@id="content"]/div[4]/div[2]/table/tbody/tr[2]/td[1]').text
Balance = wd.find_element(By.XPATH, '//*[@id="content"]/div[4]/div[2]/table/tbody/tr[2]/td[2]').text
Category =wd.find_elements(By.XPATH,)
# #Fund_name
# Units =
# Unit_value =
# ACB =
if "INTEREST" in type:

    print('Saving')
else:
    print('Fund')



