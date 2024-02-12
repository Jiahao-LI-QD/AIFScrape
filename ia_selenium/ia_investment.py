from selenium.webdriver.common.by import By
from ia_selenium import ia_fund, ia_saving, ia_selectors


def scrape_investment(wd, fund, saving):
    """
    This method takes three parameters:
    wd (WebDriver object), fund (Fund object), and saving (Saving object). The function
    is responsible for scraping investment data from a web page using Selenium.
    :param wd:chrome webdriver set up in ia_scrap.driver_setup.
    :param fund:a Pandas Dataframe setup in ia_scrap.create_table to store the scraped data.
    :param saving:a Pandas Dataframe setup in ia_scrap.create_table to store the scraped data.
    :return: return nothing, filter out the investment type and call corresponding scrape method

    Workflow:
    1.Get the XPath paths for the different elements on the web page using
    the fund_paths function from the ia_selectors module.
    2.Click on the investment page element on the web page.
    3.Find all the investment blocks on the web page.
    4.If there are no investment blocks, the investment_type can be either
    'TERMINATED' or 'EMPTY', extract the investment type from the title element
    and call the scrape function from the ia_fund module to scrape the fund data.
    5.If there are investment blocks, iterate over each block.
    6.If it is not the first block, click on the block to expand it.
    7.Extract the investment type from the block and check if it is a saving or a fund.
    8.If it is a saving, call the scrape function from the ia_saving module to scrape
    the saving data.
    9.If it is a fund, call the scrape function from the ia_fund module to scrape the fund data.
    """
    paths = ia_selectors.fund_paths()
    wd.find_element(By.XPATH, paths['investment_page']).click()
    investment_blocks = wd.find_elements(By.XPATH, paths['investment_block'])
    if len(investment_blocks) == 0:
        # if investment page does not contain any table
        title = wd.find_element(By.XPATH, paths['title']).text.split(' - ')
        if len(title) > 3:
            # if title included 'TERMINATED'
            investment_type = title[3]
        else:
            investment_type = 'EMPTY'
        ia_fund.scrape(wd, fund, investment_type, investment_blocks)
    else:
        # other regular accounts
        for number_block in range(len(investment_blocks)):
            # iterate every block
            block = investment_blocks[number_block]
            if number_block > 0:
                # for multiple blocks, expand all blocks
                block.click()
            investment_type = block.find_element(By.XPATH, paths['investment_type']).text
            if 'INTEREST' in investment_type:
                # call ia_saving method if investment type including 'INTEREST'
                ia_saving.scrape(wd, saving, investment_type, block)
            else:
                # other call ia_fund
                ia_fund.scrape(wd, fund, investment_type, block)
