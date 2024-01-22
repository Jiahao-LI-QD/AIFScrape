from selenium.webdriver.common.by import By
from ia_selenium import ia_fund, ia_saving, ia_selectors


def scrape_investment(wd, fund, saving):
    paths = ia_selectors.fund_paths()
    wd.find_element(By.XPATH, paths['investment_page']).click()
    investment_blocks = wd.find_elements(By.XPATH, paths['investment_block'])
    if len(investment_blocks) == 0:
        title = wd.find_element(By.XPATH, paths['title']).text.split(' - ')
        if len(title) > 3:
            investment_type = title[3]
        else:
            investment_type = 'EMPTY'
        ia_fund.scrape(wd, fund, investment_type, investment_blocks)
    else:
        for number_block in range(len(investment_blocks)):
            block = investment_blocks[number_block]
            if number_block > 0:
                block.click()
            investment_type = block.find_element(By.XPATH, paths['investment_type']).text
            if 'INTEREST' in investment_type:
                ia_saving.scrape(wd, saving, investment_type, block)
            else:
                ia_fund.scrape(wd, fund, investment_type, block)
