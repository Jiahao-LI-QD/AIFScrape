import time
import re
from selenium.webdriver.common.by import By

from eq_selenium import eq_selectors
from time import sleep

from utilities.companys import companies


def scrape_beneficiary(wd, beneficiary):
    time.sleep(10)
    paths = eq_selectors.beneficiary_paths()
    header = wd.find_element(By.XPATH, '//*[@id="policy_content"]/div[1]/h1[1]').text
    contract_number = re.findall(r'\((.*?)\)', header)
    print(contract_number)
    wd.find_element(By.XPATH, paths['beneficiary']).click()
    b_table = wd.find_elements(By.XPATH, paths['b_table']['b_main'])
    result = []
    for b3_row in b_table:
        b3 = [b3.text for b3 in b3_row.find_elements(By.XPATH, paths['b_table']['b_row'])]
        print(b3)
        for b in b3:
            # print(b)
            if b == '':
                continue
            bs = b.split('\n')
            print(bs)
            if len(bs)  == 8 and bs[1]=="Plan" and bs[3]=="Designation" and bs[-3]=="Percentage":
                b_item = [bi for index, bi in enumerate(bs) if index % 2 == 0]
                result = [contract_number[0], None, b_item[-2], b_item[0], float(b_item[-1].strip('%')) / 100, None,
                          None, None, companies['EQ']]
                beneficiary.loc[len(beneficiary)] = result

            if len(bs) == 7 and bs[-2]=="Percentage":
                b_item = [bs[0], bs[4]]
                result = [contract_number[0], None, b_item[-1], b_item[0],None, None,None, None, companies['EQ']]
                beneficiary.loc[len(beneficiary)] = result

            if len(bs) == 7 and bs[-4]=="Designation":
                b_item = [bs[0], bs[-1]]
                result=[contract_number[0], None,None, b_item[0], float(b_item[-1].strip('%')) / 100, None,None, None, companies['EQ']]
                beneficiary.loc[len(beneficiary)] = result

            if len(bs) == 7 and bs[-5]=="Designation" and bs[-3]=="Percentage":
                b_item = [bs[0], bs[-4],bs[-2]]
                result = [contract_number[0], None, b_item[1], b_item[0], float(b_item[-1].strip('%')) / 100, None, None,
                          None, companies['EQ']]
                beneficiary.loc[len(beneficiary)] = result
            if len(bs) == 6 and bs[-3] == "Designation" and bs[1] == "Plan":
                b_item = [bs[0], bs[-2]]
                result = [contract_number[0], None, b_item[-1], b_item[0], None, None, None, None, companies['EQ']]
                beneficiary.loc[len(beneficiary)] = result
            # if  len(bs)==5 and bs[-3]=="Designation":
            #     b_item = [bs[0], bs[-2]]
            #     result = [contract_number[0], None, b_item[-1], b_item[0], None, None, None, None, companies['EQ']]
            #     beneficiary.loc[len(beneficiary)] = result


            if (len(bs)==4 and bs[-3]=="Designation")or(len(bs)==5 and bs[-3]=="Designation"):
                b_item = [bs[0], bs[-2]]
                result = [contract_number[0], None, b_item[-1], b_item[0], None, None, None, None, companies['EQ']]
                beneficiary.loc[len(beneficiary)] = result

            if len(bs) <= 3 or (len(bs)==4 and bs[1]=="Plan"):
                b_item = [bs[0]]
                result = [contract_number[0], None, None, b_item[0], None, None, None, None, companies['EQ']]
                beneficiary.loc[len(beneficiary)] = result



