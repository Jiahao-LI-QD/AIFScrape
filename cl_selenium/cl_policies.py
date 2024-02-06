import time

from selenium.webdriver.common.by import By


def get_serial_number(wd):
    # clear filter
    time.sleep(3)

    wd.find_element(By.XPATH, '//*[@id="full-data-grid-7-row0-col1"]/div/div/a').click()

    wd.find_element(By.XPATH, '//*[@id="report-00O5o000000XMr4EAG"]/div/div[1]/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div/button').click()

    input()
    wd.find_element(By.XPATH, '//*[@id="report-00O5o000000XMr4EAG"]/div/div[1]/div[2]/div/div/div/div/div/div/div['
                              '1]/div/div/div[3]/div/div/div/div/div/div/div/div[2]/div/div[2]/ul/li['
                              '4]/div/div/div/div/div/button').click()
