import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from eq_selenium import eq_selectors, eq_holdings, eq_transaction, eq_client, eq_participant, eq_beneficiary
from utilities.web_driver import driver_setup


def login(wd, confs):

    parameters = confs['parameters']
    # wd = driver_setup(confs)
    wait = WebDriverWait(wd, 30)
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

def eq_loop_actions(wd, confs, contract_number_, tables):
    wd.get(confs['parameters']['index_url'] + contract_number_)
    if confs['control_unit'] & 1:
        eq_holdings.scrape_holdings(wd, tables['fund'])
    if confs['control_unit'] & 2:
        eq_transaction.scrape_transaction(wd, tables['transaction'],contract_number_)
    if confs['control_unit'] & 4:
        eq_client.scrape_client(wd, tables['client'],contract_number_)
        eq_participant.scrape_participant(wd, tables['participant'],contract_number_)
        eq_beneficiary.scrape_beneficiary(wd, tables['beneficiary'],contract_number_)