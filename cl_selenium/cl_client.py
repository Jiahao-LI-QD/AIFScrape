from selenium.webdriver.common.by import By
from cl_selenium import cl_beneficiary, cl_participant
from cl_selenium import cl_selectors,cl_participant,cl_beneficiary
from time import sleep

def scrape_client(wd, client):
    paths = cl_selectors.client_paths()
    contract_number=wd.find_element(By.XPATH,paths['contract_number']).text

    wd.find_element(By.XPATH, paths['client_account']).click()
    sleep(10)

    wd.find_element(By.XPATH, paths['client_hide']).click()
    c_item1 = wd.find_elements(By.XPATH, paths['client_c1']['c1_main'])
    for c_item in c_item1:
        c1 = [c.text.split('\n', 2)[1] for c in c_item.find_elements(By.XPATH, paths['client_c1']['c1_row'])]
        # print(c1)
    c_item2 = wd.find_elements(By.XPATH, paths['client_c2']['c2_main'])
    for c_item in c_item2:
        c2 = [c.text.split('\n', 1)[1] for c in c_item.find_elements(By.XPATH, paths['client_c2']['c2_row'])]
        # print(c2)
    province = wd.find_element(By.XPATH, paths['client_province']).text
    # print(province)
    address = wd.find_element(By.XPATH, paths['client_address']).text
    # print(address)

    c_item3 = wd.find_elements(By.XPATH, paths['client_c3']['c3_main'])
    for c_item in c_item3:
        c3 = [c.text for c in c_item.find_elements(By.XPATH, paths['client_c3']['c3_row'])]
        # print(c3)
    result = [c1[0], None, None, c2[0], c1[-1], address, None, None, province, None, c3[2], c3[-1], None, c3[1], c3[0],
              None,contract_number,'CL']

    # print(result)
    client.loc[len(client)] = result
    wd.back()
    return client


