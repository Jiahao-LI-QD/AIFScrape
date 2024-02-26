import time
import re
from selenium.webdriver.common.by import By

from eq_selenium import eq_selectors
from time import sleep


from utilities.companys import companies

def scrape_beneficiary(wd,beneficiary):
    time.sleep(10)
    paths = eq_selectors.beneficiary_paths()
    header = wd.find_element(By.XPATH, '//*[@id="policy_content"]/div[1]/h1[1]').text
    contract_number =re.findall(r'\((.*?)\)',header)
    # print(contract_number)
    wd.find_element(By.XPATH, paths['beneficiary']).click()
    b_table = wd.find_elements(By.XPATH, paths['b_table']['b_main'])

    for b3_row in b_table:
        b3 = [b3.text for b3 in b3_row.find_elements(By.XPATH, paths['b_table']['b_row'])]
        # print(b3)
        for b in b3:
            bs = b.split('\n')
            b_item = [bi for index, bi in enumerate(bs) if index % 2 == 0]
            if b_item[0] == '':
                continue
            if len(b_item) > 2:
                result = [contract_number[0], None, b_item[2], b_item[0], b_item[-1], None, None, None, companies['EQ']]
            else:
                result = [contract_number[0], None, None, b_item[0], None, None, None, None, companies['EQ']]
            return result
