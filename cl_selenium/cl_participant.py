from selenium.webdriver.common.by import By
from cl_selenium import cl_selectors

def scrape_participant(wd,participant):
    """
    Defines a function named scrape that is used to scrape "participant" data from a web page using Selenium.
    :param wd: chrome webdriver set up in cl_scrap.driver_setup.
    :param participant: a Pandas Dataframe setup in cl_scrap.create_table to store the scraped data.
    :return: update the participant Dataframe with the scraped data.

    Workflow:
    1.Get the XPaths for the elements to be scraped using cl_selectors.participant_paths().
    2.Find the contract number element on the web page using the XPath and extract its text.
    3.Click on the element to unhide it.
    4.Find the participant table elements on the web page using the XPath.
    5.For each row in the participant table, extract the text from the elements and create a list.
    6.Append the contract number, participant details, and 'CL' to the list.
    7.Add the list as a new row to the participant DataFrame.
    8.Return the updated participant DataFrame.


    """
    paths = cl_selectors.participant_paths()
    contract_number = wd.find_element(By.XPATH, paths['contract_number']).text
    # print(contract_number)
    wd.find_element(By.XPATH, paths['participant_hide']).click()
    p_item = wd.find_elements(By.XPATH, paths['participant_table']['participant_main'])
    for p_row in p_item:
        row = [p.text.split('\n', 1)[0] for p in
               p_row.find_elements(By.XPATH, paths['participant_table']['participant_row'])]
        result = [contract_number, row[0], row[1], row[-1],'CL']
        # print(result)
        participant.loc[len(participant)]=result
    return participant