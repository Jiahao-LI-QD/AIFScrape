import time

import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dbutilities.dbColumns import contract_columns
from eq_selenium.eq_selectors import policy_paths


def get_advisor_codes(wd, paths):
    result = []
    wait = WebDriverWait(wd, 10)

    # click magnifier button
    wait.until(EC.element_to_be_clickable((By.XPATH, paths['magnifier_button']))).click()

    # loop the table
    # - looking for rows in the column
    # - click next page
    while True:
        rows = wd.find_elements(By.XPATH, paths['code_table_rows'])
        for row in rows:
            result.append(row.text)
        next_page = wd.find_elements(By.XPATH, paths['next_advisor_page'])
        if 'disabled' in next_page[-2].get_attribute('class'):
            break
        next_page[-2].click()
        # the table is
        time.sleep(3)

    wd.find_element(By.XPATH, paths['close_advisor_page']).click()

    # get the list , remove the duplicates
    result = list(dict.fromkeys(result))

    return result


def get_policies(wd, confs):
    paths = policy_paths()
    contracts = pd.DataFrame(columns=contract_columns)
    # get policy url
    wd.get(confs['parameters']['policy_url'])

    # click search
    wd.find_element(By.XPATH, paths['export_all']).click()
    # TODO: get csv


    return contracts
