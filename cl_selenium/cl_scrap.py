import sys
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from cl_selenium import cl_selectors


# Login for Canada Life Advisor Workspace
def login(wd, user, password):
    paths = cl_selectors.login_paths()
    wait = WebDriverWait(wd, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, paths['username'])))
    wd.find_element(By.XPATH, paths['username']).send_keys(user)
    wd.find_element(By.XPATH, paths['password']).send_keys(password)
    time.sleep(1)
    wd.find_element(By.XPATH, paths['sign_in_button']).click()

    print(f"user : {user} login successful!")