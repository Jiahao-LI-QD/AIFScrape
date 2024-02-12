from selenium.webdriver.common.by import By
from ia_selenium import ia_beneficiary, ia_participant
from ia_selenium import ia_selectors


def scrape(wd, client, beneficiary, participant, contract_number):
    """
    Defines a function named scrape that is used to scrape "client" data from a web page using Selenium.

    :param wd: chrome webdriver set up in ia_scrap.driver_setup.
    :param client: a Pandas Dataframe setup in ia_scrap.create_table to store the scraped data.
    :param beneficiary: a Pandas Dataframe setup in ia_scrap.create_table to store the scraped data.
    :param participant: a Pandas Dataframe setup in ia_scrap.create_table to store the scraped data.
    :param contract_number: from ia_beneficiary.scrape function
    :return: update the client Dataframe with the scraped data.

    Workflow:
    1.Retrieve the paths for the elements on the web page using the client_paths function from the ia_selectors module.
    2.Call the ia_beneficiary.scrape() function to scrape beneficiary data using the WebDriver object and the beneficiary dictionary.
    3.Call the ia_participant.scrape() function to scrape participant data using the WebDriver object and the participant dictionary.
    4.Click on the element on the web page for into client page.
    5.Find all the client rows in the table using the XPath path for the main client table.
    6.Extract the text from each client row and store it in a list.
    7.Append the contract number to the list of client data.
    8.Append the list to the client DataFrame.
    """
    paths = ia_selectors.client_paths()

    wd.find_element(By.XPATH, paths['contract_specifications']).click()
    ia_beneficiary.scrape(wd, beneficiary)
    ia_participant.scrape(wd, participant)

    wd.find_element(By.XPATH, paths['personal_information']).click()

    Client_list = wd.find_elements(By.XPATH, paths['table_client']['main_client'])
    client_ = [Client_row.find_element(By.XPATH, paths['table_client']['row_client']).text for Client_row in Client_list]
    client_.append(contract_number)
    client_.append('IA')
    client.loc[len(client)] = client_

