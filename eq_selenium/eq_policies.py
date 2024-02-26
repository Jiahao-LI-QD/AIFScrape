import os
import time

import pandas as pd
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dbutilities.dbColumns import contract_columns
from eq_selenium.eq_scrap import login
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


def get_policies(confs):
    paths = policy_paths()
    contracts = pd.DataFrame(columns=contract_columns)
    wd = login(confs)
    # get policy url
    wd.get(confs['parameters']['policy_url'])

    wait = WebDriverWait(wd, 60)
    # click search
    wait.until(EC.element_to_be_clickable((By.XPATH, paths['search_button']))).click()
    # click export
    actions = ActionChains(wd)
    export_all=wd.find_element(By.XPATH, paths['export_all'])
    actions.move_to_element(export_all).perform()

    wait.until(EC.element_to_be_clickable((By.XPATH, paths['export_all']))).click()
    time.sleep(10)
    export_all = pd.read_csv(os.path.join(confs['csvs'], 'export_documents.csv'))
    export_all[['First Name', 'Last Name']] = [x.rsplit(' ', 1) for x in export_all['Client Name']]
    contracts['Applicant_last_name'] = export_all['Last Name']
    contracts['Applicant_first_name'] = export_all['First Name']
    contracts['Birthday'] = export_all['Birthdate']
    contracts['Contract_number'] = export_all['Policy'].apply(lambda x : str(x))
    contracts['Type'] = export_all['Registration']
    contracts['Representative_name'] = export_all['Agent Name']
    contracts['Product'] = export_all['Product']
    contracts = contracts.loc[contracts['Contract_number'].str.startswith('6')]
    contracts.reset_index(drop=True, inplace=True)
    wd.close()
    return contracts
