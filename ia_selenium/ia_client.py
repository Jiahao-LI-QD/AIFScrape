from selenium.webdriver.common.by import By
from ia_selenium import ia_beneficiary, ia_participant
from ia_selenium import ia_selectors


def scrape(wd, client, beneficiary, participant, contract_number):
    paths = ia_selectors.client_paths()

    wd.find_element(By.XPATH, paths['contract_specifications']).click()
    ia_beneficiary.scrape(wd, beneficiary)
    ia_participant.scrape(wd, participant)

    wd.find_element(By.XPATH, paths['personal_information']).click()

    Client_list = wd.find_elements(By.XPATH, paths['table_client']['main_client'])
    client_ = [Client_row.find_element(By.XPATH, paths['table_client']['row_client']).text for Client_row in Client_list]
    client_.append(contract_number)
    client.loc[len(client)] = client_

