import time
from locale import atof

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ia_selenium import ia_selectors


def scrape_transaction(wd, transactions, issue_date):
    """
    Defines a function named scrape_transaction that is used to scrape transaction data from a web page using Selenium.
    :param wd: chrome webdriver set up in ia_scrap.driver_setup.
    :param transactions: a Pandas Dataframe setup in ia_scrap.create_table to store the scraped data.
    :param issue_date: contract issue date from the Excel file to get all transactions for the client.
    :return: no return, update the transactions Dataframe with the scraped data.

    Workflow:
    1. Click on the transaction button on the web page.
    2. Wait until the table header is visible, indicating that the page has finished loading.
    3. Input the issue_date into the date input field and click the refresh button.
    4. Extract the contract number from the web page and split it to keep only the 10 digits between ' - '.
    5. Check if there are any transactions available. If not, exit the function.
    6. If there are transactions, scrape the data from the table and append it to the transaction DataFrame.
    7. If there are more pages of transactions, click the next page button and repeat steps 2-6 until all scraped.
    8. Scroll to the top of the page so the next step in scrape_traverse can be executed.
    """

    paths = ia_selectors.transactions_path()
    wd.find_element(By.XPATH, paths['transaction_button']).click()

    # Wait until the entire page finishes loading
    wait = WebDriverWait(wd, 30)
    wait.until(EC.visibility_of_element_located((By.XPATH, paths['table_header'])))
    time.sleep(1)

    # Inputting "From" date
    issue_date_element = wd.find_element(By.XPATH, paths['issue_date'])
    issue_date_element.clear()
    issue_date_element.send_keys(issue_date)
    wd.find_element(By.XPATH, paths['refresh_Button']).click()

    # Scrap contract number and keep only the 10 digits between ' - '
    text = wd.find_element(By.XPATH, paths['contract_number_account_type']).text
    contract_number = text.split(' - ')[1]

    # If transaction is empty.
    has_transaction = wd.find_element(By.XPATH, paths['has_transaction']).text
    if 'transactions' not in has_transaction:
        # grab contents of the transaction table
        table = wd.find_elements(By.XPATH, paths['table_data'])
        for row in table:
            rows = row.find_elements(By.XPATH, ".//*")
            result = [cell.text for cell in rows]

            new_row = [contract_number]
            new_row.extend(result)
            if new_row[-2] != "":
                new_row[-1] = atof(new_row[-1].replace(',', ''))
                new_row[-2] = atof(new_row[-2].replace(',', ''))
            elif len(new_row) == 8:
                new_row.pop(4)
            transactions.loc[len(transactions)] = new_row

        # for "Next" button when there is more than one page of transactions
        while len(wd.find_elements(By.CSS_SELECTOR, paths['CSS_next_page'])) > 0:
            next_page_button = wd.find_element(By.CSS_SELECTOR, paths['CSS_next_page'])
            next_page_button.click()

            # Wait until the entire page finishes loading
            wait = WebDriverWait(wd, 30)
            wait.until(EC.visibility_of_element_located((By.XPATH, paths['table_header'])))
            time.sleep(1)

            table = wd.find_elements(By.XPATH, paths['table_data'])
            for row in table:
                rows = row.find_elements(By.XPATH, ".//*")
                result = [cell.text for cell in rows]

                entire_row = [contract_number]
                entire_row.extend(result)
                if entire_row[-2] != "":
                    entire_row[-1] = atof(entire_row[-1].replace(',', ''))
                    entire_row[-2] = atof(entire_row[-2].replace(',', ''))
                elif len(entire_row) == 8:
                    entire_row.pop(4)
                transactions.loc[len(transactions)] = entire_row

        wd.execute_script("window.scrollTo(0, 0)")
