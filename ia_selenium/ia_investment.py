from selenium.webdriver.common.by import By
from ia_selenium import ia_fund, ia_saving, ia_selectors


def scrape_investment(wd, fund, saving):
    paths = ia_selectors.fund_paths()
    wd.find_element(By.XPATH, '//*[@id="Placements"]/a').click()

    try:
        investment_type = wd.find_element(By.XPATH, paths['investment_type']).text
    except Exception as e:
        title = wd.find_element(By.XPATH, paths['title']).text.split(' - ')
        if len(title) > 3:
            investment_type = title[3]
        else:
            investment_type = 'EMPTY'

    if 'INTEREST' in investment_type:
        ia_saving.scrape(wd, saving)
    else:
        ia_fund.scrape(wd, fund, investment_type)
