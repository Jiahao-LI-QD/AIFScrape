import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from ia_selenium import ia_selectors

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


def login(wd, user, password, thread='Main'):
    """
    The function is responsible for logging in a user by interacting with the web page elements using Selenium.

    :param wd: the web driver object used to interact with the web page
    :param user: the username of the user to log in
    :param password: the password of the user to log in.
    :param thread: the name of the thread (default is "Main")
    :return: None

    Flow
    1. The function retrieves the XPath selectors for various elements from the ia_selectors module.
    2. It clicks on the "Sign In" button on the web page.
    3. If a cookie consent message is displayed, it waits for the cookie button to be clickable and then clicks on it to accept the cookies.
    4. It enters the username in the appropriate input field.
    5. It moves the mouse cursor to the submit button and clicks on it.
    6. It enters the password in the appropriate input field.
    7. It moves the mouse cursor to the password submit button and clicks on it.
    8. It prints a success message indicating that the user has been logged in.
    """
    paths = ia_selectors.login_paths()

    wd.find_element(By.XPATH, paths['sign_in_button']).click()
    time.sleep(1)
    # accept cookies
    if len(wd.find_elements(By.CSS_SELECTOR, paths['cookie_consent'])) > 0:
        wait = WebDriverWait(wd, 10)  # seconds want to wait
        wait.until(
            EC.element_to_be_clickable((By.XPATH, paths['cookie_button']))
        ).click()

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
