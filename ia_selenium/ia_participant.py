from selenium.webdriver.common.by import By
from ia_selenium import ia_selectors


def scrape(wd, participant):
    """
    Defines a function named scrape that is used to scrape "participant" data from a web page using Selenium.
    :param wd: chrome webdriver set up in ia_scrap.driver_setup.
    :param participant: a Pandas Dataframe setup in ia_scrap.create_table to store the scraped data.
    :return: update the participant Dataframe with the scraped data.

    Workflow:
    1.Retrieve the XPaths for the contract number and participant elements from the ia_selectors module.
    2.Get the contract number from the web page using the XPath.
    3.Get a list of participant elements from the web page using the XPath.
    4.Iterate over each participant element.
    5.Extract the text from specific elements within each participant element.
    6.Create a list of extracted information for each participant.
    7.Append the  list to the participant DataFrame.

    """
    paths = ia_selectors.participant_paths()
    Contract_number = wd.find_element(By.XPATH, paths['contract_number']).text
    Participant_list = wd.find_elements(By.XPATH, paths['table_participant']['main_participant'])
    for Participant_row in Participant_list:
        items = [b.text for b in
                 Participant_row.find_elements(By.XPATH, paths['table_participant']['items_participant'])]
        Participants = [Contract_number, items[0], items[1], items[-1]]
        participant.loc[len(participant)] = Participants

