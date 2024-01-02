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

input()