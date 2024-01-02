import datetime
from selenium.webdriver.common.by import By


def scrape(wd, saving):

    wd.find_element(By.XPATH,'//*[@id="Placements"]').click()
    type = wd.find_element(By.XPATH,'//*[@id="content"]/div[4]/div[1]/div/div[1]').text

    text = wd.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[1]/div/span').text
    date_text = wd.find_element(By.XPATH, '//*[@id="content"]/div[3]').text.split(' ', 2)[2]
    date_obj = datetime.strptime(date_text, '%B %d, %Y')
    formatted_date = date_obj.strftime('%Y-%m-%d')
    Contract_number = text.split(' - ')[1]
    Account_type = text.split(' - ')[2]
    Investment_type = wd.find_element(By.XPATH, '//*[@id="content"]/div[4]/div[1]/div/div[1]').text
    Rate = wd.find_element(By.XPATH, '//*[@id="content"]/div[4]/div[2]/table/tbody/tr[2]/td[1]').text
    Balance = wd.find_element(By.XPATH, '//*[@id="content"]/div[4]/div[2]/table/tbody/tr[2]/td[2]').text

    print(formatted_date, Contract_number, Account_type, Investment_type, Rate, Balance)
