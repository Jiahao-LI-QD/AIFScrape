import re
import time
from datetime import datetime
from time import sleep
import pandas as pd

from selenium.webdriver.common.by import By

from eq_selenium import eq_scrap, eq_selectors
from dbutilities import dbColumns
from eq_selenium.eq_scrap import login
from utilities.companys import companies
from utilities.get_confs import get_confs
from utilities.web_driver import driver_setup
from utilities import get_account

# scraping for investment
# confs = get_confs(companies['EQ'])
# wd = login(confs)
# wd.get(confs['parameters']['index_url'] + '600468391')


def scrape_holdings(wd, holdings):
    paths = eq_selectors.holdings_paths()
    statement_date = datetime.today().strftime('%Y-%m-%d')
    text = wd.find_element(By.XPATH, paths['text']).text.split(' (', 1)
    if len(text) > 1:
        investment_type = text[0]
        policy_number = text[1][:-1]
    else:
        investment_type = None
        policy_number = ''.join(s.replace('(', '').replace(')', '') for s in text)
    account_type = wd.find_element(By.XPATH, paths['account_type']).text
    result = [statement_date, policy_number, account_type, investment_type]

    row = wd.find_elements(By.XPATH, paths['table_data'])
    data = [data.text for data in row]
    raw = [data[i:i + 6][:2] + [data[i + 3]] + [data[i:i + 6][-2].replace('$', '')] + data[i:i + 6][-1:] for i in
           range(0, len(data), 6)]

    if raw == []:
        result.append('TERMINATED')
        raw = [[None] * 5]

    else:
        result.extend([None])

    final_result = []
    for raw_list in raw:
        final_result.append(result + raw_list + [None, 'EQ'])

    return final_result

# df = pd.DataFrame(final_result, columns=dbColumns.fund_columns)
# print(df)
# holdings = pd.concat([holdings,df], ignore_index=True)
# return holdings
