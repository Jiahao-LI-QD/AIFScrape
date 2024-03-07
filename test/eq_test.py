# import time
# from datetime import datetime
# from time import sleep
# import pandas as pd
#
# from selenium.webdriver.common.by import By
#
# from eq_selenium import eq_scrap, eq_selectors,eq_holdings
# from eq_selenium import eq_scrap, eq_client, eq_participant, eq_beneficiary
# from dbutilities import dbColumns
# from eq_selenium.eq_scrap import login
# from utilities.companys import companies
# from utilities.get_confs import get_confs
# from eq_selenium.eq_policies import get_policies
# from eq_selenium.eq_scrap import login
# from utilities.companys import companies
# from utilities.get_confs import get_confs
# from utilities.web_driver import driver_setup
# from utilities import get_account
#
# confs=get_confs(companies['EQ'])
# contracts=get_policies(confs)
# wd=login(confs)
# for index,contract in contracts.iterrows():
#
#     wd.get(confs['parameters']['index_url']+contract['Contract_number'])
#     print(contract['Contract_number'])
#     time.sleep(10)
#
#     holdings = pd.DataFrame(columns=dbColumns.fund_columns)
#     test_holdings = eq_holdings.scrape_holdings(wd, holdings)
#     pd.set_option('display.max_columns', None)
#     # print(test_holdings)
#     #
#     # client = pd.DataFrame(columns=dbColumns.client_columns)
#     # test_client = eq_client.scrape_client(wd, client)
#     # # pd.set_option('display.max_columns', None)
#     # print(test_client)
#     #
#     # participant = pd.DataFrame(columns=dbColumns.participant_columns)
#     # test_participant = eq_participant.scrape_participant(wd, participant)
#     # pd.set_option('display.max_columns', None)
#     # print(test_participant)
#     #
#     # beneficiary = pd.DataFrame(columns=dbColumns.beneficiary_columns)
#     # test_beneficiary = eq_beneficiary.scrape_beneficiary(wd, beneficiary)
#     # pd.set_option('display.max_columns', None)
#     # print(test_beneficiary)




import os
import traceback

import pandas as pd

from dbutilities import dbColumns
from dbutilities.dbColumns import transaction_columns, fund_columns, participant_columns, beneficiary_columns, \
    client_columns
from eq_selenium import eq_holdings, eq_client, eq_participant, eq_beneficiary
from eq_selenium.eq_beneficiary import scrape_beneficiary
from eq_selenium.eq_client import scrape_client
from eq_selenium.eq_holdings import scrape_holdings
from eq_selenium.eq_participant import scrape_participant
from eq_selenium.eq_policies import get_policies
from eq_selenium.eq_scrap import login
from eq_selenium.eq_transaction import scrape_transaction
from utilities.companys import companies
from utilities.get_confs import get_confs


confs = get_confs(companies['EQ'])

policies = get_policies(confs)

wd = login(confs)
# transaction = pd.DataFrame(columns=transaction_columns)
holdings = pd.DataFrame(columns=fund_columns)
# participant = pd.DataFrame(columns=participant_columns)
# beneficiary = pd.DataFrame(columns=beneficiary_columns)
# client = pd.DataFrame(columns=client_columns)
for policy in policies.drop_duplicates(subset=['Contract_number'])['Contract_number']:
    try:
        print(policy)
        wd.get(confs['parameters']['index_url'] + policy)
        scrape_holdings(wd, holdings)
        # scrape_client(wd, client)
        # scrape_beneficiary(wd, beneficiary)
        # scrape_participant(wd, participant)
        # scrape_transaction(wd, transaction, policy)
    except Exception as e:
        print(e)
        traceback.print_exc()
        wd.close()
        wd = login(confs)

    # holdings = pd.DataFrame(columns=dbColumns.fund_columns)
    # test_holdings = eq_holdings.scrape_holdings(wd, holdings)
    # pd.set_option('display.max_columns', None)
    # print(test_holdings)
    #
    # client = pd.DataFrame(columns=dbColumns.client_columns)
    # test_client = eq_client.scrape_client(wd, client)
    # pd.set_option('display.max_columns', None)
    # print(test_client)
    #
    # participant = pd.DataFrame(columns=dbColumns.participant_columns)
    # test_participant = eq_participant.scrape_participant(wd, participant)
    # pd.set_option('display.max_columns', None)
    # print(test_participant)
    #
    # beneficiary = pd.DataFrame(columns=dbColumns.beneficiary_columns)
    # test_beneficiary = eq_beneficiary.scrape_beneficiary(wd, beneficiary)
    # pd.set_option('display.max_columns', None)
    # print(test_beneficiary)

# transaction.to_csv(os.path.join(confs['csvs'], 'transactions.csv'))
holdings.to_csv(os.path.join(confs['csvs'], 'fund.csv'))
# participant.to_csv(os.path.join(confs['csvs'], 'part.csv'))
# beneficiary.to_csv(os.path.join(confs['csvs'], 'bene.csv'))
# client.to_csv(os.path.join(confs['csvs'], 'client.csv'))
