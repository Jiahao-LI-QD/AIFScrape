import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://translate.google.com/")

input_area = driver.find_element(By.XPATH, "//textarea[@class='er8xn']")
input_area.send_keys("nevertheless")
driver.find_element(By.XPATH, "//button[contains(@class,\'VfPpkd-Bz112c-LgbsSe\') and @aria-label=\'More source languages\']").click()
#driver.find_element(By.XPATH, "//button[contains(@class,\'VfPpkd-Bz112c-LgbsSe\') and @aria-label=\'More target languages\']").click()

# TODO : fix input exception
# SOLUTION: THERE ARE two EXACT same input <- get by elements or Search XPath more exact
chinese = driver.find_elements(By.XPATH, "//input[@class='yFQBKb' and @aria-label='Search languages' and @jsname='oA4zhb']")
chinese[0].send_keys("english")
time.sleep(1)
chinese[0].send_keys(Keys.ENTER)

time.sleep(3)

driver.find_element(By.XPATH, "//button[contains(@class,\'VfPpkd-Bz112c-LgbsSe\') and @aria-label=\'More target languages\']").click()
time.sleep(3)
chinese[1].send_keys("chinese")
chinese[1].send_keys(Keys.ENTER)

time.sleep(10)
output = driver.find_element(By.XPATH, "//span[@class='ryNqvb']")
print(output.text)

# <input aria-label="Search languages" class="yFQBKb" jsaction="input:G0jgYd;" jsname="oA4zhb" placeholder="Search languages" type="text">

# <input aria-label="Search languages" class="yFQBKb" jsaction="input:G0jgYd;" jsname="oA4zhb" placeholder="Search languages" type="text">