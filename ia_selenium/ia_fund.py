from datetime import datetime
from locale import atof

import pandas as pd
from dbutilities import dbColumns
from selenium.webdriver.common.by import By
from ia_selenium import ia_selectors


def scrape(wd, fund, investment_type):
    # ["Statement_Date", "Contract_number", "Account_type", "Investment_type"
    # "Category", "Fund_name", "Units", "Unit_value", "Value", "ACB"]
    paths = ia_selectors.fund_paths()

    statement_date = wd.find_element(By.XPATH, paths['statement_date']).text.split(" ", 2)[2]
    formatted_date = datetime.strptime(statement_date, '%B %d, %Y').strftime('%Y-%m-%d')

    title = wd.find_element(By.XPATH, paths['title']).text.split(' - ')

    contract_number, account_type = title[1:3]

    if investment_type in ['TERMINATED', 'EMPTY']:
        row = [formatted_date, contract_number, account_type, investment_type]
        row.extend([None] * 6)
        fund.loc[len(fund)] = row
    else:
        tb = wd.find_elements(By.XPATH, paths['table_body']['main_body'])
        category_type = ""
        for t in tb:
            if t.get_attribute('style') == r'display: none;' or t.get_attribute('class') == 'footerRow':
                continue

            elements = t.find_elements(By.XPATH, paths['table_body']['table_rows'])
            if elements[0].get_attribute('class') == 'classificationfondfu':
                category_type = t.text
                continue
            else:
                # fund_name, units, unit_value, value, acb = elements[:4]
                table_columns = [child.text for child in elements]
                row = [formatted_date, contract_number, account_type, investment_type, category_type]

                if account_type in ['TFSA', 'FHSA']:
                    row.extend(table_columns[1:5])
                    row.append(None)
                else:
                    row.extend(table_columns[1:6])
                row[-3] = atof(row[-3].replace(',', ''))
                row[-4] = atof(row[-4].replace(',', ''))
                fund.loc[len(fund)] = row
