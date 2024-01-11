from selenium.webdriver.common.by import By
from ia_selenium import ia_selectors

def scrape(wd, beneficiary):
    paths = ia_selectors.beneficiary_paths()
    Contract_number = wd.find_element(By.XPATH, paths['contract_number']).text
    Beneficiary_Category=wd.find_element(By.XPATH, paths['beneficiary_Category']).text
    Beneficiary_list = wd.find_elements(By.XPATH, paths['table_beneficiary']['main_beneficiary'])
    for Beneficiary_row in Beneficiary_list:
        items = [b.text for b in Beneficiary_row.find_elements(By.XPATH, paths['table_beneficiary']['items_beneficiary'])]

        #Beneficiary_name = Beneficiary_row.find_element(By.XPATH, paths['table_beneficiary']['name_beneficiary']).text
        #Allocation = float(Beneficiary_row.find_element(By.XPATH, paths['table_beneficiary']['allocation_beneficiary']).text.strip('%'))/100
        if 'RESP' in Beneficiary_Category:
            result = [Contract_number, Beneficiary_Category, items[0], float(items[1].strip('%'))/100, None, None, items[-1]]
            #Birthday = Beneficiary_row.find_element(By.XPATH, paths['table_beneficiary']['birthday_beneficiary']).text
        else:
            result = [Contract_number, Beneficiary_Category, items[0], float(items[1].strip('%')) / 100, items[2],
                      items[-1], None]


            #Relationship = Beneficiary_row.find_element(By.XPATH, paths['table_beneficiary']['relationship_beneficiary']).text
            #Benefit_class = Beneficiary_row.find_element(By.XPATH, paths['table_beneficiary']['class_beneficiary']).text
        beneficiary.loc[len(beneficiary)] = result
