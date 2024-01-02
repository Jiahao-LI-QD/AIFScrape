from selenium.webdriver.common.by import By


def scrape(wd, fund):

    tb = wd.find_elements(By.XPATH, '//*[@id="content"]/div[4]/div[2]/table/tbody/*')
