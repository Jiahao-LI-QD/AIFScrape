from selenium.webdriver.common.by import By
from ia_selenium import ia_selectors
from utilities.companys import companies


def scrape(wd, beneficiary):
    """
    Defines a function named scrape that is used to scrape "beneficiary" data from a web page using Selenium.

    :param wd: chrome webdriver set up in ia_scrap.driver_setup.
    :param beneficiary: a Pandas Dataframe setup in ia_scrap.create_table to store the scraped data.
    :return: update the beneficiary Dataframe with the scraped data.

    Workflow:
    1.Retrieve the paths for the elements on the web page using the beneficiary_paths function from the ia_selectors module.
    2.Get the contract number from the web page by finding the element using the XPath.
    3.Get the beneficiary category from the web page by finding the element using the XPath.
    4.Get the list of beneficiary rows from the web page.
    5.Iterate over each beneficiary row.
    6.For each row, extract the items
    7.If the beneficiary category contains 'RESP', create a result list with corresponding columns .
    8.If the beneficiary category does not contain 'RESP',create a result list with corresponding columns .
    9.Append the result list to the beneficiary DataFrame.
    """
    paths = ia_selectors.beneficiary_paths()
    Contract_number = wd.find_element(By.XPATH, paths['contract_number']).text
    Beneficiary_Category = wd.find_element(By.XPATH, paths['beneficiary_Category']).text
    Beneficiary_list = wd.find_elements(By.XPATH, paths['table_beneficiary']['main_beneficiary'])
    for Beneficiary_row in Beneficiary_list:
        items = [b.text for b in
                 Beneficiary_row.find_elements(By.XPATH, paths['table_beneficiary']['items_beneficiary'])]

        if 'RESP' in Beneficiary_Category:
            result = [Contract_number, Beneficiary_Category, None, items[0], float(items[1].strip('%')) / 100, None,
                      None, items[-1], companies['iA']]

        else:
            result = [Contract_number, Beneficiary_Category, None, items[0], float(items[1].strip('%')) / 100, items[2],
                      items[-1], None, companies['iA']]

        beneficiary.loc[len(beneficiary)] = result
