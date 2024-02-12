from selenium import webdriver
import os


def driver_setup(parameters, head=False):
    """
    Set up the webdriver accordingly and return it
    :param parameters: 'parameters' in confs which is returned by ia_get_config
    :param head: does it need to be headless mode
    :return: webdriver that is configured properly
    """
    # start web driver
    # Initializes Chrome options for the web driver.
    chrome_options = webdriver.ChromeOptions()
    # set the default download directory to the contracts folder
    prefs = {'download.default_directory': os.path.join(parameters['csv_path'], parameters['contracts'])}
    chrome_options.add_experimental_option('prefs', prefs)
    if not head:
        chrome_options.add_argument('headless')
    wd = webdriver.Chrome(chrome_options)
    wd.implicitly_wait(15)
    return wd
