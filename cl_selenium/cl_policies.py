import os
import time

import pandas as pd
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from cl_selenium.cl_scrap import login
from cl_selenium.cl_selectors import policies_paths
from cl_selenium.cl_utilities import split_investment_type
from utilities.web_driver import driver_setup


def get_serial_number(confs):
    """
    This code defines a function named get_serial_number that retrieves serial numbers from a web page using
    Selenium. It sets up the web driver, logs in to the website, and performs actions to filter and scrape data from
    the policies table.

    :param confs: A dictionary containing the confs
    :return: tables

    Flow
    1. The function sets up the web driver using the driver_setup function.
    2. It navigates to the policies URL and logs in using the login function.
    3. It retrieves the paths for various elements on the page using the policies_paths function.
    4. It clears the filter on the policies table.
    5. It clicks the filter button to open the filter options.
    6. It clicks the clear search button to remove any existing search filters.
    7. It closes the filter options.
    8. It removes subtotals and grand totals from the table.
    9. It enters a loop to scrape the serial numbers from the table.
    10. It scrolls down to load more rows and continues scraping until all rows have been processed.
    11. Save the policies table to csv file and return it
    """
    # setup driver and login to the policies table
    wd = driver_setup(confs['parameters'], confs['head_mode'])
    login(wd, confs['parameters']['username'], confs['parameters']['password'])
    wd.get(confs['parameters']['policies_url'])
    paths = policies_paths()

    # clear filter
    time.sleep(10)
    wait = WebDriverWait(wd, 10)
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, 'iframe')))

    # click filter
    wd.find_element(By.XPATH, paths['filter_button']).click()
    time.sleep(1)

    # click clear search
    wd.find_element(By.CSS_SELECTOR, paths['clear_search']).click()
    time.sleep(1)

    # close filter
    wd.find_element(By.XPATH, paths['filter_button']).click()

    # remove subtotals
    # wd.find_element(By.XPATH, paths['subtotal_button']).click()
    # remove grand totals
    # wd.find_element(By.XPATH, paths['grand_total_button']).click()
    # At the beginning of loop there is no last-serial number
    policies = pd.DataFrame(columns=['Name', 'policy_number', 'fund_name', 'account_type', 'advisor'])
    last_serial = ''
    while True:
        # while ended, jump out of loop
        last_serial, ended = loop_list(wd, paths, policies, last_serial)
        if ended:
            break
    policies.to_csv(os.path.join(confs['csvs'], "cl_policies.csv"))
    wd.close()
    return policies


def loop_list(wd, paths, policies, last_serial=''):
    """
    The loop_list function is responsible for scraping data from a table on a web page using Selenium. It loops
    through the rows of the table, extracts the necessary information, and performs certain actions based on the
    extracted data.

    :param policies: dataframe for recording the policies
    :param wd: webdriver instance
    :param paths: the css or Xpath paths
    :param last_serial: the last serial number of the previous loop
    :return last_serial: return the last serial number of the table
    :return ended: if this is the end of polices return True, False otherwise

    Flow:
    Prepare the actions for the scroll action later.
    Initialize variables for scraping.
    Get the rows of the table.
    Slice the rows to remove unnecessary rows.
    Check if there is a duplicate contract number.
    Loop through each row and extract the necessary information.
    Check if the investment is not insurance and not empty.
    Print the extracted information.
    Update the last serial number.
    Scroll down to load more rows.
    Return the updated last serial number and a flag indicating if the loop should end.
    prepare the actions for the scroll action later
    """

    actions = ActionChains(wd)

    # initialize the variables for scrape
    account_name = ''
    ended = False

    # get row content
    rows = wd.find_elements(By.XPATH, paths['table']['rows'])

    # The rows from table need to be sliced, set up the start and the end
    slice_start = 0
    slice_end = -1
    # remove the first header row
    if 'data-grid-header-row' in rows[slice_start].get_attribute('class'):
        slice_start += 1
    # remove the first and last spacer whice have no content for scrape
    if rows[slice_start].get_attribute('class') == 'data-grid-table-row-spacer':
        slice_start += 1
    if rows[slice_end].get_attribute('class') != 'data-grid-table-row-spacer':
        # if there is no spacer at the end, the loop should end
        ended = True
        slice_end = len(rows)
    rows = rows[slice_start:slice_end]

    # skip the duplicate contract numbers
    if last_serial == '':
        new_row = True
    else:
        new_row = False

    # start to loop through
    for row in rows:
        # find all the text under the row
        columns = row.find_elements(By.XPATH, paths['table']['columns_of_row'])[:-1]
        if len(columns) > 4:
            # get the <a> under the account name
            account_name = columns[0].find_element(By.XPATH, paths['table']['account_name']).text
            columns = columns[1:]
        texts = [c.text for c in columns]
        texts.insert(0, account_name)
        # check the investment is not insurance and it is not empty
        if new_row and not ('insurance' in texts[3] or texts[3] == '-'):
            del texts[1]
            invest, i_type = split_investment_type(texts[2])
            texts[2] = invest
            texts.insert(3, i_type)
            policies.loc[len(policies)] = texts
            last_serial = texts[1]
        if not new_row and texts[2] == last_serial:
            new_row = True
    # scroll down
    actions.move_to_element(rows[-1]).perform()
    return last_serial, ended
