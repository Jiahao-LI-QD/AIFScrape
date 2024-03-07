from selenium.webdriver.common.by import By
from cl_selenium import cl_beneficiary, cl_participant
from cl_selenium import cl_selectors,cl_participant,cl_beneficiary
from time import sleep

from utilities.companys import companies
from datetime import datetime

def scrape_client(wd, client):
    """
    Defines a function named scrape that is used to scrape "client" data from a web page using Selenium.
    :param wd: chrome webdriver set up in cl_scrap.driver_setup.
    :param client: a Pandas Dataframe setup in cl_scrap.create_table to store the scraped data.
    :return: update the client Dataframe with the scraped data.

    Workflow:
    1.Get the XPaths for the elements to be scraped using cl_selectors.client_paths().
    2.Extract the contract number from the web page.
    3.Click on the client account element.
    4.Wait for 5 seconds.
    5.Click on the client hide element.
    6.Extract the client data from the web page
    7.Create a result list with the extracted data.
    8.Add the result list to the client DataFrame.
    9.Go back to the previous page.
    10.Return the updated client DataFrame.
    """
    paths = cl_selectors.client_paths()
    # wd.find_element(By.XPATH, paths['summary_button']).click()
    contract_number=wd.find_element(By.XPATH,paths['contract_number']).text

    wd.find_element(By.XPATH, paths['client_account']).click()
    sleep(5)

    if wd.find_element(By.XPATH, paths['client_kind']).text=='Individual':
        wd.find_element(By.XPATH, paths['client_hide']).click()

    # province = wd.find_element(By.XPATH, paths['client_province']).text
    r3 = wd.find_elements(By.XPATH, paths['client_r3'])
    if r3:
        province=r3[0].text
    else:
        r3=None


    c_item1 = wd.find_elements(By.XPATH, paths['client_c1']['c1_main'])
    for c_item in c_item1:
        c1 = [c.text.split('\n', 2)[1] for c in c_item.find_elements(By.XPATH, paths['client_c1']['c1_row'])]
        # print(c1)
    c_item2 = wd.find_elements(By.XPATH, paths['client_c2']['c2_main'])
    for c_item in c_item2:
        c2 = [c.text.split('\n', 1)[1] for c in c_item.find_elements(By.XPATH, paths['client_c2']['c2_row'])]
        # print(c2)

    # print(province)

    # address = wd.find_element(By.XPATH, paths['client_address']).text
    address = wd.find_elements(By.XPATH, paths['client_address'])
    if address:
        address=address[0].text
    else:
        address=None
    # print(address)

    c_item3 = wd.find_elements(By.XPATH, paths['client_c3']['c3_main'])
    for c_item in c_item3:
        c3 = [c.text for c in c_item.find_elements(By.XPATH, paths['client_c3']['c3_row'])]
        # print(c3)
    if wd.find_element(By.XPATH, paths['client_kind']).text == 'Individual':
        result = [c1[0], None, None, c2[0], datetime.strptime(c1[-1],"%B %d, %Y").strftime("%Y-%m-%d"), address, None, None, province, None, c3[2], c3[-1], None, c3[1], c3[0],
              None,contract_number, companies['CL']]
    else:
        result=[c1[0],None,None,c1[-1],None,address,None,None,c2[0],None,None,None,None,c3[0],None,None,contract_number, companies['CL']]

    # print(result)
    client.loc[len(client)] = result
    wd.back()
    return client


