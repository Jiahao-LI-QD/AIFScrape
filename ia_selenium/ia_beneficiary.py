from selenium.webdriver.common.by import By
def scrape(wd, beneficiary):
    wd.find_element(By.XPATH, '//*[@id="Specifications"]/a').click()
    Contract_number = wd.find_element(By.XPATH, '//*[@id="content"]/div[3]/table[1]/tbody/tr[1]/td[2]').text
    Beneficiary_list = wd.find_elements(By.XPATH, '//*[@id="content"]/div[3]/div[2]/table/tbody/tr')
    for Beneficiary_row in Beneficiary_list:
        Beneficiary_name = Beneficiary_row.find_element(By.XPATH, './td[1]').text
        Allocation = Beneficiary_row.find_element(By.XPATH, './td[2]').text
        Relationship = Beneficiary_row.find_element(By.XPATH, './td[3]').text
        Benefit_class = Beneficiary_row.find_element(By.XPATH, './td[4]').text
        beneficiary.loc[len(beneficiary)] = [Contract_number, Beneficiary_name, Allocation, Relationship, Benefit_class]
    print(beneficiary)