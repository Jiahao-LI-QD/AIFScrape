import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from eq_selenium import eq_selectors
from utilities.web_driver import driver_setup


def login(confs):

    parameters = confs['parameters']
    wd = driver_setup(parameters, confs['head_mode'])
    wait = WebDriverWait(wd, 10)
    wd.get(parameters['login_url'])
    paths = eq_selectors.login_paths()
    wait.until(EC.presence_of_element_located((By.XPATH, paths['username'])))
    wd.find_element(By.XPATH, paths['username']).send_keys(parameters['username'])
    wd.find_element(By.XPATH, paths['continue_button']).click()
    time.sleep(1)
    actions = ActionChains(wd)

    wd.find_element(By.XPATH, paths['password']).send_keys(parameters['password'])
    login_button = wd.find_element(By.XPATH, paths['login_button'])
    actions.move_to_element(login_button).perform()
    login_button.click()
    wait.until(EC.presence_of_element_located((By.XPATH, paths['main_page'])))

    print(f"user : {parameters['username']} login successful!")
    return wd
