import os
import time

import pandas as pd
from selenium.webdriver.common.by import By

from ia_selenium import ia_selectors
from ia_selenium.ia_scrap import ia_app
from utilities.web_driver import driver_setup


def click_contract_list(confs):
    """
    This method request downloads of contract list for different groups
    :param confs: ia_confs loaded at the start of ia_app
    :return: nothing

    Workflow:
    1.Set up the web driver using the parameters from confs.
    2.Call the ia_app function to log into the IA website.
    3.Get the paths for various elements on the website.
    4.Click on the "My Client" button --> "Group" button.
    5.Wait for the website response and select the first group.
    6.Click on the "Download" option --> "Search" button --> "Submit" button
    7.Click on the "My Client" button --> "Group" button.
    8.Wait for the website response and select the second group.
    9.Repeat Step 6
    10.Print a success message.

    """
    wd = driver_setup(confs)
    ia_app(wd, confs['parameters'])
    paths = ia_selectors.download_path()
    wd.find_element(By.XPATH, paths['myclient_button']).click()
    wd.find_element(By.XPATH, paths['group']).click()
    time.sleep(3)
    # waiting website response, selecting the first group
    wd.find_element(By.XPATH, paths['FV6_group']).click()
    wd.find_element(By.XPATH, paths['download_option']).click()
    wd.find_element(By.XPATH, paths['search_button']).click()
    wd.find_element(By.XPATH, paths['submit_button']).click()
    wd.find_element(By.XPATH, paths['myclient_button']).click()
    wd.find_element(By.XPATH, paths['group']).click()
    time.sleep(3)
    # waiting website response, selecting the second group
    wd.find_element(By.XPATH, paths['GK4_group']).click()
    wd.find_element(By.XPATH, paths['download_option']).click()
    wd.find_element(By.XPATH, paths['search_button']).click()
    wd.find_element(By.XPATH, paths['submit_button']).click()
    print('Download request successfully submitted')
    pass


def save_contract_list(confs):
    """
    This method downloads the contract lists from website,
    combines them as a single file and renames to today's date,
    old files are removed at the end
    :param confs: dictionary generated from ia_conf
    :return: files are combined and  renamed to format as 'date_today' +  '_contracts.xlsx'

    Workflow:
    1.Set up the web driver using the driver_setup function.
    2.Call the ia_app function to log in to the website.
    3.Click on the mailbox button --> first file link --> download file button.
    4.Get the filename of the downloaded file.
    5.Click on the next button --> second file link --> download file button.
    6.Get the filename of the downloaded file.
    7.Read the contents of the downloaded files using pd.read_excel.
    8.Concatenate the dataframes and ignore the first two rows of the second dataframe.
    9.Generate the new filename by combining the date_today and '_contract.xlsx'.
    10.Remove the old downloaded files.
    11.Save the concatenated dataframe to the new filename as an Excel file.
    """

    paths = ia_selectors.save_path()
    wd = driver_setup(confs)
    ia_app(wd, confs)
    wd.find_element(By.XPATH, paths['mailbox_button']).click()
    wd.find_element(By.XPATH, paths['file_link1']).click()
    wd.find_element(By.XPATH, paths['download_file']).click()
    filename1 = wd.find_element(By.XPATH, paths['download_file']).text
    wd.find_element(By.XPATH, paths['next_button']).click()
    time.sleep(3)
    wd.find_element(By.XPATH, paths['file_link2']).click()
    if not confs['head_mode']:
        wd.find_element(By.XPATH, paths['download_file']).click()
    time.sleep(3)
    filename2 = wd.find_element(By.XPATH, paths['download_file']).text
    time.sleep(3)
    df1 = pd.read_excel(os.path.join(confs['csvs'], filename1))
    df2 = pd.read_excel(os.path.join(confs['csvs'], filename2))
    df_total = pd.concat([df1, df2[2:]], ignore_index=True)
    result = confs['date_today'] + '_contract.xlsx'
    new_filename = os.path.join(confs['csvs'], result)
    os.remove(
        os.path.join(confs['csvs'], filename1)
    )
    os.remove(
        os.path.join(confs['csvs'], filename2)
    )
    df_total.to_excel(str(new_filename), index=False)
    print('File saved')
    return result
