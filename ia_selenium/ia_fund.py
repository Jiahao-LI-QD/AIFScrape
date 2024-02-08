from datetime import datetime
from locale import atof

import pandas as pd
from dbutilities import dbColumns
from selenium.webdriver.common.by import By
from ia_selenium import ia_selectors


def scrape(wd, fund, investment_type, block):
    """
    If funds exist in investment page, extracts fund data from investment page storing it in the Fund DataFrame.
    :param wd: chrome webdriver set up in ia_scrap.driver_setup.
    :param fund: a Pandas Dataframe setup in ia_scrap.create_table to store the scraped data.
    :param investment_type: a variable saved from ia_investment.scrape_investment to determine the investment type or
                            defunct account.
    :param block: a list of web elements on the top right of the page that contains name, account number & investment type.
    :return: no return, update the transactions Dataframe with the scraped data.

    Fund Dataframe structure: ["Statement_Date", "Contract_number", "Account_type", "Investment_type", "Category",
    "Fund_name", "Units", "Unit_value", "Value", "ACB"]

    Workflow:
    1. Extract the statement date from the web page and format it as 'YYYY-MM-DD'.
    2. Extract the contract number and account type from the web page.
    3. If the investment type is 'TERMINATED' or 'EMPTY', add the empty row to the DataFrame.
    4. If the investment type is not 'TERMINATED' or 'EMPTY', find the table body elements within the block.
    5. Iterate over the table body elements and skip elements with style 'display: none;' or class 'footerRow'.
    6. For each table body element, extract the table rows and check if the first element has class 'classificationfondfu'.
    7. If the first element has class 'classificationfondfu', update the category type.
    8. If the first element does not have class 'classificationfondfu', extract the table data elements and create a row.
    9. If the account type is 'NON-REGISTERED', extend the row with the table columns from index 0 to 4.
    10. If the account type is not 'NON-REGISTERED', extend the row with the table columns from index 0 to 3 and append None to the row.
    11. Convert the last two elements of the row to float by removing commas and store the row in the DataFrame.
    """

    paths = ia_selectors.fund_paths()

    statement_date = wd.find_element(By.XPATH, paths['statement_date']).text.split(" ", 2)[2]
    formatted_date = datetime.strptime(statement_date, '%B %d, %Y').strftime('%Y-%m-%d')

    title = wd.find_element(By.XPATH, paths['title']).text.split(' - ')

    contract_number, account_type = title[1:3]

    if investment_type in ['TERMINATED', 'EMPTY']:
        row = [formatted_date, contract_number, account_type, investment_type]
        row.extend([None] * 7)
        fund.loc[len(fund)] = row
    else:
        tb = block.find_elements(By.XPATH, paths['table_body']['main_body'])
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
                elements = t.find_elements(By.XPATH, paths['table_body']['table_data'])
                table_columns = [child.text for child in elements]
                row = [formatted_date, contract_number, account_type, investment_type, category_type]
                #
                # if category_type == 'Diversified Funds':
                #     row.extend(table_columns[0].split(" - ", 2))
                #     row.extend(table_columns[1:4])
                #     row.append(None)
                if account_type == 'NON-REGISTERED':
                    row.extend(table_columns[0].split(" - ", 2))
                    row.extend(table_columns[1:5])
                else:
                    row.extend(table_columns[0].split(" - ", 2))
                    row.extend(table_columns[1:4])
                    row.append(None)
                row[-3] = atof(row[-3].replace(',', ''))
                row[-4] = atof(row[-4].replace(',', ''))
                fund.loc[len(fund)] = row
