from datetime import datetime
from selenium.webdriver.common.by import By
from ia_selenium import ia_selectors
from utilities.companys import companies


def scrape(wd, saving, investment_type, block):
    """
    This method extracting saving investments from IA website
    :param wd: chrome webdriver set up in ia_scrap.driver_setup.
    :param saving: a Pandas Dataframe setup in ia_scrap.create_table to store the scraped data.
    :param investment_type: type of investment being scraped (fund or saving)
    :param block: WebElement object representing a block of data on the web page.
    :return: nothing return; update the saving Dataframe with the scraped data.

    Workflow:
    1.Extracts the statement date from the web page and converts it to the desired format.
    2.Retrieves the contract number and account type from the web page.
    3.If the investment type is "GUARANTEED INTEREST FUNDS",
    it iterates over the table rows and extracts the data.
    4.If the investment type is not "GUARANTEED INTEREST FUNDS",
    it sets values not find on web table to None and extracts the interest rate and balance.
    5.Converts the interest rate from a percentage to a decimal.
    6.Appends the extracted data to the saving DataFrame.
    """
    paths = ia_selectors.saving_paths()

    # statement date
    date_text = wd.find_element(By.XPATH, paths['date_text']).text.split(' ', 2)[2]
    date_obj = datetime.strptime(date_text, '%B %d, %Y')
    formatted_date = date_obj.strftime('%Y-%m-%d')

    # contract number and account type
    text = wd.find_element(By.XPATH, paths['contract_number_account_type']).text
    contract_number = text.split(' - ')[1]
    account_type = text.split(' - ')[2]
    # investment_type extracted from ia_investment
    row = [formatted_date, contract_number, account_type, investment_type]

    if 'GUARANTEED INTEREST FUNDS' in investment_type:
        # if saving investment type is 'GUARANTEED INTEREST FUNDS', extract the table data
        tb = block.find_elements(By.XPATH, paths['table_body']['main_body'])
        for t in tb:
            if t.get_attribute('style') == r'display: none;' or t.get_attribute('class') == 'footerRow':
                continue
            table_body = t.text.split(' ')
            row = [formatted_date, contract_number, account_type, investment_type]
            row.extend(table_body)
    else:
        # for other saving investment type, extract available data and assgin none to missing data
        row = [formatted_date, contract_number, account_type, investment_type]
        row.extend([None] * 4)
        row.append(block.find_element(By.XPATH, paths['rate']).text)
        row.append(None)
        row.append(block.find_element(By.XPATH, paths['balance']).text)

    # convert number from percentage to decimal
    row[8] = float(row[8].strip('%')) * 0.01
    row.append(companies['iA'])
    saving.loc[len(saving)] = row

