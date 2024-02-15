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
    wait = WebDriverWait(wd, 15)
    wait.until(EC.presence_of_element_located((By.XPATH, paths['username'])))
    wd.find_element(By.XPATH, paths['username']).send_keys(user)
    wd.find_element(By.XPATH, paths['password']).send_keys(password)
    time.sleep(1)
    wd.find_element(By.XPATH, paths['sign_in_button']).click()

    print(f"user : {user} login successful!")


def ia_loop_actions(wd, paths, confs, contract_number, tables, start_date):
    """

    :param wd:
    :param paths:
    :param confs:
    :param contract_number:
    :param tables:
    :param start_date:
    :return:
    """
    wd.find_element(By.XPATH, paths['myclient_button']).click()

    wd.find_element(By.XPATH, paths['contract_number_input']).clear()

    wd.find_element(By.XPATH, paths['contract_number_input']).send_keys(contract_number)

    wd.find_element(By.XPATH, paths['search_button']).click()

    if confs['control_unit'] & 1:
        ia_investment.scrape_investment(wd, tables['fund'], tables['saving'])
    if confs['control_unit'] & 2:
        ia_transactions.scrape_transaction(wd, tables['transaction'], start_date)
    if confs['control_unit'] & 4:
        ia_client.scrape(wd, tables['client'], tables['beneficiary'], tables['participant'],
                         contract_number)
