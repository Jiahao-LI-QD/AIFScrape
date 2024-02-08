from selenium.webdriver.common.by import By
from cl_selenium import cl_selectors

def scrape_beneficiary(wd,beneficiary):
    paths = cl_selectors.beneficiary_paths()
    contract_number = wd.find_element(By.XPATH, paths['contract_number']).text

    b_item = wd.find_elements(By.XPATH, paths['beneficiary_table']['beneficiary_main'])

    for b_row in b_item:
        row = [b.text for b in b_row.find_elements(By.XPATH, paths['beneficiary_table']['beneficiary_row'])]
        result = [contract_number, None, row[0], row[1], row[-1], row[2], row[3], None, 'CL']
        # print(result)
        beneficiary.loc[len(beneficiary)]=result

    wd.execute_script("window.scrollTo(0, 0)")

    return beneficiary