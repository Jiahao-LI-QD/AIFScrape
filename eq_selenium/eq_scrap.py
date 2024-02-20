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
    password = wd.find_element(By.XPATH, paths['password'])
    actions.move_to_element(password).perform()
    password.click()

    print(f"user : {user} login successful!")
