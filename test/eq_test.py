import time
from datetime import datetime
from time import sleep
import pandas as pd

from selenium.webdriver.common.by import By

from eq_selenium import eq_scrap, eq_selectors,eq_holdings
from eq_selenium import eq_scrap, eq_client, eq_participant, eq_beneficiary
from dbutilities import dbColumns
from eq_selenium.eq_scrap import login
from utilities.companys import companies
from utilities.get_confs import get_confs
from eq_selenium.eq_policies import get_policies
from eq_selenium.eq_scrap import login
from utilities.companys import companies
from utilities.get_confs import get_confs
from utilities.web_driver import driver_setup
from utilities import get_account

confs=get_confs(companies['EQ'])
contracts=get_policies(confs)
wd=login(confs)
for index,contract in contracts.iterrows():

    wd.get(confs['parameters']['index_url']+contract['Contract_number'])
    print(contract['Contract_number'])
    time.sleep(10)

    holdings = pd.DataFrame(columns=dbColumns.fund_columns)
    test_holdings = eq_holdings.scrape_holdings(wd, holdings)
    pd.set_option('display.max_columns', None)
    print(test_holdings)

    client = pd.DataFrame(columns=dbColumns.client_columns)
    test_client = eq_client.scrape_client(wd, client)
    pd.set_option('display.max_columns', None)
    print(test_client)

    participant = pd.DataFrame(columns=dbColumns.participant_columns)
    test_participant = eq_participant.scrape_participant(wd, participant)
    pd.set_option('display.max_columns', None)
    print(test_participant)

    beneficiary = pd.DataFrame(columns=dbColumns.beneficiary_columns)
    test_beneficiary = eq_beneficiary.scrape_beneficiary(wd, beneficiary)
    pd.set_option('display.max_columns', None)
    print(test_beneficiary)





