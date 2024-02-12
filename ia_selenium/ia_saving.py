from datetime import datetime
from selenium.webdriver.common.by import By
from ia_selenium import ia_selectors


def scrape(wd, saving, investment_type, block):
    paths = ia_selectors.saving_paths()

    # statement date
    date_text = wd.find_element(By.XPATH, paths['date_text']).text.split(' ', 2)[2]
    date_obj = datetime.strptime(date_text, '%B %d, %Y')
    formatted_date = date_obj.strftime('%Y-%m-%d')

    # contract number and account type
    text = wd.find_element(By.XPATH, paths['contract_number_account_type']).text
    contract_number = text.split(' - ')[1]
    account_type = text.split(' - ')[2]
    row = [formatted_date, contract_number, account_type, investment_type]

    if 'GUARANTEED INTEREST FUNDS' in investment_type:
        tb = block.find_elements(By.XPATH, paths['table_body']['main_body'])
        for t in tb:
            if t.get_attribute('style') == r'display: none;' or t.get_attribute('class') == 'footerRow':
                continue
            table_body = t.text.split(' ')
            row = [formatted_date, contract_number, account_type, investment_type]
            row.extend(table_body)
    else:
        row = [formatted_date, contract_number, account_type, investment_type]
        row.extend([None] * 4)
        row.append(block.find_element(By.XPATH, paths['rate']).text)
        row.append(None)
        row.append(block.find_element(By.XPATH, paths['balance']).text)

    row[8] = float(row[8].strip('%')) * 0.01
    saving.loc[len(saving)] = row

