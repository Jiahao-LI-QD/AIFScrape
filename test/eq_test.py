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
confs = get_confs(companies['EQ'])
wd = login(confs)
wd.get(confs['parameters']['index_url'] + '600468391')
paths = eq_selectors.holdings_paths()
statement_date = datetime.today().strftime('%Y-%m-%d')
text = wd.find_element(By.XPATH, paths['text']).text.split(' (', 1)
policy_number = text[1][:-1]
investment_type = text[0]
account_type = wd.find_element(By.XPATH, paths['account_type']).text
result = [statement_date, policy_number, account_type, investment_type]

row = wd.find_elements(By.XPATH, paths['table_data'])
data = [data.text for data in row]
raw = [data[i:i + 6][:2] + [data[i + 3]] + [data[i:i + 6][-2].replace('$', '')] + data[i:i + 6][-1:] for i in
       range(0, len(data), 6)]

if raw == []:
    result.append('TERMINATED')
    raw = [[None]*5]

else:
    result.extend([None])

final_result = []
print(raw)
for raw_list in raw:
    final_result.append(result + raw_list + [None, 'EQ'])

df = pd.DataFrame(final_result, columns=dbColumns.fund_columns)
print(df)

# check if it is a table
# if elements[1].get_attribute('class') == "sm-show no-print":
#     result.extend([None])
#     for element in elements:
# #         details_block = element.find_elements(By.XPATH, './div[2]/*')
# #         for row in details_block:
# #             data = row.find_elements(By.XPATH, './*')
# #             if len(data) > 1 and data[0].tag_name == 'p':
# #                 for item in data:
# #                     print("Value:", item.text)
# #             # for item in data:
# #             #     if len(data) > 1 and data[0].tag_name == 'p':
# #             #         fund_name = item.text
# #             #         print(fund_name)
#
#
#
#
# else:
#     category = 'TERMINATED'
#     result.append(category)

# print(result)
