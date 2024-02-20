from time import sleep
import pandas as pd

from selenium.webdriver.common.by import By

from eq_selenium import eq_scrap
from dbutilities import dbColumns
from utilities.web_driver import driver_setup
from utilities import get_account

# save cl_conf as parameters
parameters = get_account.account("eq_conf")

# set up Chrome driver
wd = driver_setup(parameters, True)
wd.get(parameters['web_url'])
sleep(1)

# testing for log in function
eq_scrap.login(wd, parameters['username'], parameters['password'])