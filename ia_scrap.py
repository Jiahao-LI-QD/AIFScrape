from selenium import webdriver
from selenium.webdriver.common.by import By
from ia_selenium import ia_login

wd = webdriver.Chrome()

wd.implicitly_wait(15)

wd.get('https://iaa.secureweb.inalco.com/MKMWPN23/home')

ia_login.login(wd)

# TODO read csv to find contract number

wd.find_element(By.XPATH, '//*[@id="ContractNumber"]').send_keys('1819806281')

wd.find_element(By.XPATH, '//*[@id="btnSearch"]').click()



