import time
from datetime import datetime

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import calendar
from selenium.webdriver.support import expected_conditions as EC


def eq_transaction(wd, transaction):
    row_number = 0
    wait = WebDriverWait(wd, 15)
    time.sleep(5)
    transaction_button = wd.find_element(By.XPATH, '//*[@id="Transactions"]')
    # wait.until(EC.element_to_be_clickable(transaction_button)).click()

    while (len(wd.find_elements(By.XPATH, '//*[@id="update_period"]'))) == 0:
        time.sleep(1)
        transaction_button.click()
    time.sleep(5)
    actions = ActionChains(wd)
    month_to_num = {name: num for num, name in enumerate(calendar.month_name) if num}
    update_button = wd.find_element(By.XPATH, '//*[@id="update_period"]')
    start_date = wd.find_element(By.XPATH, '//*[@id="policy_content"]/div[3]/div[2]/p[2]')
    start_month = int(month_to_num[start_date.split(' ')[0]]) - 1
    start_year = int(start_date.split(', ')[-1])
    end_month = datetime.now().month - 1
    end_year = datetime.now().year
    selections = []
    for year in range(start_year, end_year + 1):
        for i in range(4):
            if year == start_year and i < (start_month // 3):
                continue
            if year == end_year and i * 3 > end_month:
                break
            selections.append([i * 3, year, i * 3 + 2, year])
    selections.reverse()
    date_range = wd.find_element(By.XPATH, '//*[@id="periodSelection"]')
    Select(date_range).select_by_value('custom')
    result = []
    for selection in selections:
        Select(wd.find_element(By.XPATH, '//*[@id="from_month"]')).select_by_index()
        time.sleep(5)
        rows = wd.find_elements(By.XPATH, '//*[@id="policy_details"]/div[@class="Transactions"]/div/div[2]/div[2]/table/tbody/tr')
        for row in rows:
            result.append(row.text)
    # wd.find_element(By.XPATH, '//*[@id="policy_details"]/div[4]/div/div[2]/div[2]/table/tbody/tr')
