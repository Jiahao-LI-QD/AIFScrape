import time
from datetime import datetime
from time import sleep
import pandas as pd

from selenium.webdriver.common.by import By

from eq_selenium import eq_scrap, eq_selectors,eq_holdings
from dbutilities import dbColumns
from eq_selenium.eq_scrap import login
from utilities.companys import companies
from utilities.get_confs import get_confs
from utilities.web_driver import driver_setup
from utilities import get_account

# scraping for investment

confs = get_confs(companies['EQ'])
wd = login(confs)
wd.get(confs['parameters']['index_url'] + '600468391')

holdings = pd.DataFrame(columns=dbColumns.fund_columns)
test_holdings = eq_holdings.scrape_holdings(wd, holdings)
pd.set_option('display.max_columns', None)
print(test_holdings)


