from selenium.webdriver.common.by import By
from ia_selenium import ia_selectors


def scrape(wd, participant):
    paths = ia_selectors.participant_paths()
    Contract_number = wd.find_element(By.XPATH, paths['contract_number']).text
    Participant_list = wd.find_elements(By.XPATH, paths['table_participant']['main_participant'])
    for Participant_row in Participant_list:
        items = [b.text for b in
                 Participant_row.find_elements(By.XPATH, paths['table_participant']['items_participant'])]
        Participants = [Contract_number, items[0], items[1], items[-1]]
        participant.loc[len(participant)] = Participants
        # Role = Participant_row.find_element(By.XPATH, paths['table_participant']['role_participant']).text
        # Participant_name = Participant_row.find_element(By.XPATH, paths['table_participant']['name_participant']).text
        # Birthday = Participant_row.find_element(By.XPATH,paths['table_participant']['birthday_participant'] ).text
        # participant.loc[len(participant)] = [Contract_number, Role, Participant_name, Birthday]
