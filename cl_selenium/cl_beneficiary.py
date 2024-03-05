from selenium.webdriver.common.by import By
from cl_selenium import cl_selectors
from utilities.companys import companies


def scrape_beneficiary(wd, beneficiary):
    """
    Defines a function named scrape that is used to scrape "beneficiary" data from a web page using Selenium.
    :param wd: chrome webdriver set up in cl_scrap.driver_setup.
    :param beneficiary: a Pandas Dataframe setup in cl_scrap.create_table to store the scraped data.
    :return: update the beneficiary Dataframe with the scraped data.

    workflow:
    1.Retrieve the paths for the elements on the web page using the beneficiary_paths function from the cl_selectors module.
    2.Get the contract number from the web page by finding the element using the XPath.
    3.Find all the beneficiary rows on the web page.
    4.For each beneficiary row, extract the data from the row and create a list of the extracted data.
    5.Create a result list by combining the contract number, the extracted data, and other required fields.
    6.Append the result list to the beneficiary DataFrame.
    7.Scroll the web page to the top.
    8.Return the updated beneficiary DataFrame.
    """
    paths = cl_selectors.beneficiary_paths()
    contract_number = wd.find_element(By.XPATH, paths['contract_number']).text

    b_item = wd.find_elements(By.XPATH, paths['beneficiary_table']['beneficiary_main'])

    for b_row in b_item:
        row = [b.text for b in b_row.find_elements(By.XPATH, paths['beneficiary_table']['beneficiary_row'])]
        result = [contract_number, None, row[0], row[1], float(row[-1].strip('%'))/100, row[2], row[3], None, companies['CL']]

        beneficiary.loc[len(beneficiary)] = result

    wd.execute_script("window.scrollTo(0, 0)")

    return beneficiary
