from selenium.webdriver.common.by import By
from ia_selenium import ia_selectors

def scrape(wd, beneficiary):
    paths = ia_selectors.beneficiary_paths()
    Contract_number = wd.find_element(By.XPATH, paths['contract_number']).text
    Beneficiary_list = wd.find_elements(By.XPATH, paths['table_beneficiary']['main_beneficiary'])
    for Beneficiary_row in Beneficiary_list:
        Beneficiary_name = Beneficiary_row.find_element(By.XPATH, paths['table_beneficiary']['name_beneficiary']).text
        Allocation = float(Beneficiary_row.find_element(By.XPATH, paths['table_beneficiary']['allocation_beneficiary']).text.strip('%'))/100
        Relationship = Beneficiary_row.find_element(By.XPATH, paths['table_beneficiary']['relationship_beneficiary']).text
        Benefit_class = Beneficiary_row.find_element(By.XPATH, paths['table_beneficiary']['class_beneficiary']).text
        beneficiary.loc[len(beneficiary)] = [Contract_number, Beneficiary_name, Allocation, Relationship, Benefit_class]
