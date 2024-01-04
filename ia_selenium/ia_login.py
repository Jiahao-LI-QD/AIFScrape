from selenium.webdriver.common.by import By
from ia_selenium import keys
from ia_selenium import ia_selectors


def login(wd, user, password):
    paths = ia_selectors.login_paths()
    wd.find_element(By.XPATH,
                    paths['sign_in_button']).click()

    wd.find_element(By.XPATH, paths['username']).send_keys(user)

    # accept cookies
    wd.find_element(By.XPATH, paths['cookie_button']).click()

    wd.find_element(By.XPATH, paths['submit_username']).click()

    wd.find_element(By.XPATH, paths['password']).send_keys(password)

    wd.find_element(By.XPATH, paths['submit_password']).click()

    print(f"user : {user} login successful!")