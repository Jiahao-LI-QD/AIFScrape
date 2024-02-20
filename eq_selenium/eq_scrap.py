import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from eq_selenium import eq_selectors


def login(wd, user, password):
    paths = eq_selectors.login_paths()
    wd.find_element(By.XPATH, paths['username']).send_keys(user)
    wd.find_element(By.XPATH, paths['continue_button']).click()
    time.sleep(1)
    actions = ActionChains(wd)

    wd.find_element(By.XPATH, paths['password']).send_keys(password)
    login_button = wd.find_element(By.XPATH, paths['login_button'])
    actions.move_to_element(login_button).perform()
    login_button.click()

    print(f"user : {user} login successful!")
