from selenium.webdriver.common.by import By
from cl_selenium import cl_selectors

def scrape_participant(wd,participant):
    paths = cl_selectors.participant_paths()
    contract_number = wd.find_element(By.XPATH, paths['contract_number']).text
    # print(contract_number)
    wd.find_element(By.XPATH, paths['participant_hide']).click()
    p_item = wd.find_elements(By.XPATH, paths['participant_table']['participant_main'])
    for p_row in p_item:
        row = [p.text.split('\n', 1)[0] for p in
               p_row.find_elements(By.XPATH, paths['participant_table']['participant_row'])]
        result = [contract_number, row[0], row[1], row[-1],'CL']
        # print(result)
        participant.loc[len(participant)]=result
    return participant