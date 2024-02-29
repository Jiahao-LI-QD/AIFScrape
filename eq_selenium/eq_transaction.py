import time
from datetime import datetime

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import calendar
from selenium.webdriver.support import expected_conditions as EC

from eq_selenium.eq_selectors import transactions_paths
from utilities.companys import companies


def eq_transaction(wd, transaction, contract_number):
    paths = transactions_paths()

    time.sleep(5)
    transaction_button = wd.find_element(By.XPATH, paths['transaction_button'])

    while (len(wd.find_elements(By.XPATH, paths['update_button']))) == 0:
        time.sleep(1)
        transaction_button.click()
    time.sleep(5)

    month_to_num = {name: num for num, name in enumerate(calendar.month_name) if num}

    start_date = wd.find_element(By.XPATH, paths['start_date']).text
    start_month = int(month_to_num[start_date.split(' ')[0]])
    start_year = int(start_date.split(', ')[-1])
    end_month = datetime.now().month
    end_year = datetime.now().year

    selections = []
    for year in range(start_year, end_year + 1):
        for i in range(4):
            if year == start_year and i < (start_month - 1) // 3:
                continue
            if year == end_year and i > end_month // 3 - 1:
                selections.append([i * 3 + 1, year, end_month, year])
                break
            selections.append([i * 3 + 1, year, i * 3 + 3, year])

    selections.reverse()
    date_range = wd.find_element(By.XPATH, paths['date_range'])
    Select(date_range).select_by_value('custom')
    update_button = wd.find_element(By.XPATH, paths['update_button'])
    update_button.click()

    for selection in selections:
        from_month = selection[0]
        from_year = selection[1]
        to_month = selection[2]
        to_year = selection[3]
        Select(wd.find_element(By.XPATH, paths['from_month'])).select_by_value(str(from_month))
        Select(wd.find_element(By.XPATH, paths['from_year'])).select_by_value(str(from_year))
        Select(wd.find_element(By.XPATH, paths['to_month'])).select_by_value(str(to_month))
        Select(wd.find_element(By.XPATH, paths['to_year'])).select_by_value(str(to_year))
        update_button.click()
        time.sleep(5)

        if (wd.find_element(By.XPATH, paths['no_transaction_alert'])).get_attribute('style') == 'display: block;':
            continue

        rows = wd.find_elements(By.XPATH, paths['rows'])
        for row in rows:
            columns = [x.text for x in row.find_elements(By.XPATH, paths['columns'])]

            transaction_date = columns[0]
            transaction_type = columns[1]
            fund_code = columns[2]
            unit = float(columns[3].replace(",", ""))
            unit_value = float(columns[4].replace("$", "").replace(",", ""))
            amount = columns[5]
            row = [contract_number, transaction_date, transaction_type, fund_code, amount, unit, unit_value, companies['EQ']]
            print(row)
            transaction.loc[len(transaction)] = row
