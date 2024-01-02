from selenium.webdriver.common.by import By
from ia_selenium import ia_fund, ia_saving

def scrape_investment(wd, fund, saving):
    wd.find_element(By.XPATH, '//*[@id="Placements"]/a').click()
    if 'INTEREST' in wd.find_element(By.XPATH, '//*[@id="content"]/div[4]/div[1]/div/div[1]').text:
        ia_saving.scrape(wd, saving)
    else:
        ia_fund.scrape(wd, fund)