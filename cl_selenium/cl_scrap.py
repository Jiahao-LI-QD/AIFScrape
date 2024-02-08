import sys
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from cl_selenium import cl_selectors


# Read configs from cl_conf to get url, username, password, and folder paths
def cl_account():
    with open(os.path.join(sys.path[1], r"confs\cl_conf")) as f:
        l = [line.rstrip('\n').split("=", 1) for line in f.readlines()]
        d = {key.strip(): value.strip() for key, value in l}
    if "username" not in d or "password" not in d:
        raise Exception("CL account info not found. Please provide it in confs/cl_conf")
    if "web_url" not in d:
        raise Exception("Web url not found. Please provide it in confs/cl_conf")
    if "csv_path" not in d:
        raise Exception("File path for csv files not found. Please provide it in confs/cl_conf")
    return d


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