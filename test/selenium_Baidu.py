# download driver for chrome for testing if possible
"""
npx @puppeteer/browsers install chromedriver@canary
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

# TODO : Chrome version and driver need to be unified in group
# https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

# TODO : XPath as locator
kw_input = driver.find_element(By.ID, "kw")
kw_input.send_keys("长城")

driver.find_element(By.ID, "su").click()

time.sleep(10)
driver.quit()