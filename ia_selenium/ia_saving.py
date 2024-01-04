from datetime import datetime
from selenium.webdriver.common.by import By
from ia_selenium import ia_selectors

def scrape(wd, saving):
    paths = ia_selectors.saving_paths()
    wd.find_element(By.XPATH, paths['investment_bottom']).click()

    #statement date
    date_text = wd.find_element(By.XPATH, paths['date_text']).text.split(' ', 2)[2]
    date_obj = datetime.strptime(date_text, '%B %d, %Y')
    formatted_date = date_obj.strftime('%Y-%m-%d')

    #contract number and account type
    text = wd.find_element(By.XPATH, paths['contract_number_account_type']).text
    contract_number = text.split(' - ')[1]
    account_type = text.split(' - ')[2]

    #investment type
    investment_type = wd.find_element(By.XPATH, paths['investment_type']).text

    #rate and balance
    rate = wd.find_element(By.XPATH, paths['rate']).text
    balance = wd.find_element(By.XPATH, paths['balance']).text

    saving.loc[len(saving)] = [formatted_date, contract_number, account_type, investment_type, rate, balance]

    print(formatted_date, contract_number, account_type, investment_type, rate, balance)