from selenium.webdriver.common.by import By


def scrape(wd, participant):
    Contract_number = wd.find_element(By.XPATH, '//*[@id="content"]/div[3]/table[1]/tbody/tr[1]/td[2]').text
    Participant_list = wd.find_elements(By.XPATH, '//*[@id="content"]/div[3]/div[1]/table/tbody/tr')
    for Participant_row in Participant_list:
        Role = Participant_row.find_element(By.XPATH, './td[1]').text
        Participant_name = Participant_row.find_element(By.XPATH, './td[2]').text
        Birthday = Participant_row.find_element(By.XPATH, './td[3]').text
        participant.loc[len(participant)] = [Contract_number, Role, Participant_name, Birthday]

