from datetime import datetime
from selenium.webdriver.common.by import By


def scrape(wd, saving):
    wd.find_element(By.XPATH, '//*[@id="Placements"]').click()

    #statement date
    date_text = wd.find_element(By.XPATH, '//*[@id="content"]/div[3]').text.split(' ', 2)[2]
    date_obj = datetime.strptime(date_text, '%B %d, %Y')
    formatted_date = date_obj.strftime('%Y-%m-%d')

    #contract number and account type
    text = wd.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[1]/div/span').text
    contract_number = text.split(' - ')[1]
    account_type = text.split(' - ')[2]

    #investment type
    investment_type = wd.find_element(By.XPATH, '//*[@id="content"]/div[4]/div[1]/div/div[1]').text

    #rate and balance
    rate = wd.find_element(By.XPATH, '//*[@id="content"]/div[4]/div[2]/table/tbody/tr[2]/td[1]').text
    balance = wd.find_element(By.XPATH, '//*[@id="content"]/div[4]/div[2]/table/tbody/tr[2]/td[2]').text

    saving.loc[len(saving)] = [formatted_date, contract_number, account_type, investment_type, rate, balance]
