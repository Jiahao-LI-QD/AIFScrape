import sys
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from cl_selenium import cl_selectors, cl_holdings, cl_transactions, cl_client, cl_participant, cl_beneficiary


# Login for Canada Life Advisor Workspace
def login(wd, user, password):
    """
    responsible for logging in to a website using the provided username and password.
    :param wd: The WebDriver object that represents the browser session, initiated in web_driver.py.
    :param user: The username to be used for logging in, initiated in get_confs.py.
    :param password: The password to be used for logging in, initiated in get_confs.py.
    :return: does not return any value. print user login info.

    """
    paths = cl_selectors.login_paths()
    wd.get(paths['web_url'])
    wait = WebDriverWait(wd, 15)
    wait.until(EC.presence_of_element_located((By.XPATH, paths['username'])))
    wd.find_element(By.XPATH, paths['username']).send_keys(user)
    wd.find_element(By.XPATH, paths['password']).send_keys(password)
    time.sleep(2)
    wd.find_element(By.XPATH, paths['sign_in_button']).click()
    wait.until(EC.presence_of_element_located((By.XPATH, paths['page_load'])))
    time.sleep(2)

    print(f"user : {user} login successful!")


def cl_loop_actions(wd, paths, confs, contract_number, tables):
    """
    performs a series of actions on a web page: searches for the contract number, waits for the policy home page to load
    , and then performs different actions based on the configurations. These actions include scraping holdings,
    transactions, client information, participant information, and beneficiary information from the web page.
    :param wd: The WebDriver object that represents the browser session, initiated in web_driver.py.
    :param paths: A dictionary containing XPaths to different elements on the web page.
    :param confs: A dictionary containing configurations for the function.
    :param contract_number: The contract number to search for on the web page.
    :param tables: A dictionary containing names of tables to store scraped data.
    :return: does not return any value. It performs actions on the web page and scrapes data into the provided tables.

    Workflow:
    1. The function searches for the contract number by locating the search field element using the XPath provided.
    2. After a short delay, the function clicks the submit button to initiate the search.
    3. The function waits for the policy home page to load by waiting for the presence of the summary table element.
    4. If the first control unit is enabled (bitwise AND with 1), the function calls the scrape_holdings function from
    the cl_holdings module to scrape holdings data from the web page.
    5. If the second control unit is enabled (bitwise AND with 2), the function calls the scrape_transactions function
    from the cl_transactions module to scrape transactions data from the web page.
    6. If the third control unit is enabled (bitwise AND with 4), the function calls the scrape_client,
    scrape_participant, and scrape_beneficiary functions from the respective modules to scrape data from the web page.
    """
    # search policy number and go into account page
    paths = cl_selectors.traverse_paths()
    # wait = WebDriverWait(wd, 15)
    # wait.until(EC.presence_of_element_located((By.XPATH, paths['page_load'])))
    time.sleep(1)

    wd.find_element(By.XPATH, paths['search_field']).clear()
    wd.find_element(By.XPATH, paths['search_field']).send_keys(contract_number)
    time.sleep(2)

    # there are duplicate policies, need to find the active one out of them.
    dropdown_list = wd.find_elements(By.XPATH, paths['dropdown_layer'])
    if len(dropdown_list) < 3:
        wd.find_element(By.XPATH, paths['policy_submit']).click()
    else:
        wd.find_element(By.XPATH, paths['policy_search']).click()
        wait = WebDriverWait(wd, 15)
        wait.until(EC.presence_of_element_located((By.XPATH, paths['search_sort'])))
        time.sleep(1)

        wd.find_element(By.XPATH, paths['search_sort']).click()
        wd.find_element(By.XPATH, paths['sort_status']).click()
        wd.find_element(By.XPATH, paths['search_sort']).click()
        wd.find_element(By.XPATH, paths['sort_status']).click()
        wd.find_element(By.XPATH, paths['correct_policy']).click()

    # wait for policy home page to be loaded
    wait = WebDriverWait(wd, 15)
    wait.until(EC.presence_of_element_located((By.XPATH, paths['summary_button'])))
    time.sleep(1)

    if confs['control_unit'] & 1:
        cl_holdings.scrape_holdings(wd, tables['fund'])
    if confs['control_unit'] & 2:
        cl_transactions.scrape_transactions(wd, tables['transaction'])
    if confs['control_unit'] & 4:
        cl_client.scrape_client(wd, tables['client'])
        cl_participant.scrape_participant(wd, tables['participant'])
        cl_beneficiary.scrape_beneficiary(wd, tables['beneficiary'])
