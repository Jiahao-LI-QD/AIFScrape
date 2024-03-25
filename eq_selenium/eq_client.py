import time
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from eq_selenium import eq_selectors
from time import sleep

from utilities.companys import companies
from selenium.webdriver.support import expected_conditions as EC


def scrape_client(wd, client, contract_number):
    time.sleep(5)
    # header=wd.find_element(By.XPATH,'//*[@id="policy_content"]/div[1]/h1[1]').text
    # contract_number=re.findall(r'\((.*?)\)',header)

    wait = WebDriverWait(wd, 60)
    paths = eq_selectors.client_paths()
    wait.until(EC.element_to_be_clickable((By.XPATH, paths['owner']))).click()
    # wd.find_element(By.XPATH, paths['owner']).click()

    name = wd.find_element(By.XPATH, paths['name']).text

    if name.startswiths('MS.') or name.startswiths('MR.'):
        name = name.split('.', 1)[-1].lstrip()

    c1_table = wd.find_elements(By.XPATH, paths['c1_table']['c1_main'])
    for c1_row in c1_table:
        c1 = [c1.text for c1 in c1_row.find_elements(By.XPATH, paths['c1_table']['c1_row'])]
        address = ' '.join(c1)
    c2 = wd.find_elements(By.XPATH, paths['assigned'])
    if len(c2) == 0:
        c2_table = wd.find_elements(By.XPATH, paths['c2_table']['c2_main'])
        for c2_row in c2_table:
            c2 = [c2.text for c2 in c2_row.find_elements(By.XPATH, paths['c2_table']['c2_row'])]
            print(c2)
    else:
        c2_table = wd.find_elements(By.XPATH, paths['c3_table']['c3_main'])
        for c2_row in c2_table:
            c2 = [c2.text for c2 in c2_row.find_elements(By.XPATH, paths['c3_table']['c3_row'])]
            print(c2)

    if '@' in c2[0] and len(c2) == 1:
        result = [name, None, None, None, None, address, None, None, None, None, None, None, None, None, c2[0], None,
                  contract_number, companies['EQ']]
    if '@' in c2[-1] and len(c2) == 2:
        result = [name, None, None, None, None, address, None, None, None, None, c2[0], None, None, None, c2[-1], None,
                  contract_number, companies['EQ']]
    if '@' not in c2[-1] and len(c2) == 1:
        result = [name, None, None, None, None, address, None, None, None, None, c2[0], None, None, None, None, None,
                  contract_number, companies['EQ']]

    client.loc[len(client)] = result
