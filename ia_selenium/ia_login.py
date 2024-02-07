import time

from selenium.webdriver.common.by import By
from ia_selenium import keys
from ia_selenium import ia_selectors

from selenium.webdriver.common.action_chains import ActionChains


def login(wd, user, password, thread='Main'):
    paths = ia_selectors.login_paths()

    wd.find_element(By.XPATH, paths['sign_in_button']).click()
    time.sleep(1)
    # accept cookies
    wd.find_element(By.XPATH, paths['cookie_button']).click()

    wd.find_element(By.XPATH, paths['username']).send_keys(user)

    submit = wd.find_element(By.XPATH, paths['submit_username'])
    actions = ActionChains(wd)
    actions.move_to_element(submit).perform()
    submit.click()

    wd.find_element(By.XPATH, paths['password']).send_keys(password)

    password = wd.find_element(By.XPATH, paths['submit_password'])
    actions.move_to_element(password).perform()
    password.click()

    print(f"{thread} user : {user} login successful!")
