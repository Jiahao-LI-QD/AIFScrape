import time
import re
from selenium.webdriver.common.by import By

from eq_selenium import eq_selectors
from time import sleep


from utilities.companys import companies

def scrape_participant(wd,participant):
    time.sleep(10)
    paths = eq_selectors.participant_paths()
    header = wd.find_element(By.XPATH, '//*[@id="policy_content"]/div[1]/h1[1]').text
    contract_number = re.findall(r'\((.*?)\)',header)
    # print(contract_number)
    wd.find_element(By.XPATH, paths['annuitant']).click()
    a1_table = wd.find_elements(By.XPATH, paths['a1_table']['a1_main'])
    for a1_row in a1_table:
        a1 = [a1.text for a1 in a1_row.find_elements(By.XPATH, paths['a1_table']['a1_row'])]

    a2_table = wd.find_elements(By.XPATH, paths['a2_table']['a2_main'])
    for a2_row in a2_table:
        a2 = [a2.text for a2 in a2_row.find_elements(By.XPATH, paths['a2_table']['a2_row'])]
    result = [contract_number[0], a1[0], a1[-1], a2[-1], companies['EQ']]
    participant.loc[len(participant)]=result