from selenium import webdriver
import os


def driver_setup(confs):
    """
    Set up the webdriver accordingly and return it
    :param confs: confs loaded at the start of app
    :return: webdriver that is configured properly
    """
    # start web driver
    # Initializes Chrome options for the web driver.
    chrome_options = webdriver.ChromeOptions()
    # set the default download directory to the contracts folder
    prefs = {'download.default_directory': confs['csvs']}
    chrome_options.add_experimental_option('prefs', prefs)
    chrome_options.add_argument('--window-size=1920,1080')
    if not confs['head_mode']:
        # chrome_options.add_argument('user-agent=Chrome/122.0.6261.69')
        chrome_options.add_argument('headless')
        chrome_options.add_argument('--disable-gpu')
    wd = webdriver.Chrome(chrome_options)
    wd.implicitly_wait(15)
    return wd
