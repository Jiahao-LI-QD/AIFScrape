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

    :param wd:
    :param user:
    :param password:
    :return:
    """
    paths = cl_selectors.login_paths()
    wait = WebDriverWait(wd, 15)
    wait.until(EC.presence_of_element_located((By.XPATH, paths['username'])))
    wd.find_element(By.XPATH, paths['username']).send_keys(user)
    wd.find_element(By.XPATH, paths['password']).send_keys(password)
    time.sleep(1)
    wd.find_element(By.XPATH, paths['sign_in_button']).click()

    print(f"user : {user} login successful!")


def cl_loop_actions(wd, paths, confs, contract_number, tables):
    """

    :param wd:
    :param paths:
    :param confs:
    :param contract_number:
    :param tables:
    :return:
    """
    # search policy number and go into account page
    wd.find_element(By.XPATH, paths['search_field']).send_keys(contract_number)
    time.sleep(2)
    wd.find_element(By.XPATH, paths['policy_submit']).click()

    # wait for policy home page to be loaded
    wait = WebDriverWait(wd, 15)
    wait.until(EC.presence_of_element_located((By.XPATH, paths['summary_table'])))
    time.sleep(1)

    if confs['control_unit'] & 1:
        cl_holdings.scrape_holdings(wd, tables['fund'])
    if confs['control_unit'] & 2:
        cl_transactions.scrape_transactions(wd, tables['transaction'])
    if confs['control_unit'] & 4:
        cl_client.scrape_client(wd, tables['client'])
        cl_participant.scrape_participant(wd, tables['participant'])
        cl_beneficiary.scrape_beneficiary(wd, tables['beneficiary'])
