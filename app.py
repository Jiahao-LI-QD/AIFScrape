from datetime import datetime
import os
import sys

import pandas as pd

from dbutilities import dbColumns
from ia_selenium import keys, ia_scrap

# set up the control unit & recovery_file unit
control_unit = 1
if len(sys.argv) > 1:
    control_unit = int(sys.argv[1])
if control_unit not in range(1, 8):
    print(f"The control model is not supported, will use default scrape mode")

if control_unit & 1:
    print("Task: Scrape Investments")
if control_unit & 2:
    print("Task: Scrape Transactions")
if control_unit & 4:
    print("Task: Scrape Clients Information")
print("======================")

# Get required parameters for ia_app
try:
    ia_parameters = keys.ia_account()
except Exception as e:
    print(e)
    exit()

date_today = "{:%Y_%m_%d_%H_%M_%S}".format(datetime.now())

csvs = os.path.join(ia_parameters['csv_path'], date_today)

# make directory for current scarpy process
try:
    os.mkdir(csvs)
    print(f"Create {ia_parameters['csv_path']}\\{date_today} directory!")
except Exception as e:
    print(f"The directory {ia_parameters['csv_path']}\\{date_today} already exist!")

# TODO: read contract from today's contract list
# get contract numbers for ia company
ia_contracts = pd.read_excel(os.path.join(ia_parameters['csv_path'], ia_parameters['contracts'], 'contracts_0.XLSX')).iloc[2:]
ia_contracts.columns = dbColumns.contract_columns

# start the ia company scrapy process
ia_wd = ia_scrap.ia_app(ia_parameters)

# create dataframes for all the tables
tables = ia_scrap.create_table(control_unit)


tables['contracts'] = ia_contracts
tables['recover'] = []

# do - while loop to traverse through the contract numbers until no exception
iteration_time = 1
while iteration_time < 4:
    ia_scrap.scrape_traverse(ia_wd, control_unit, tables, csvs, iteration_time)
    if len(tables['recover']) == 0:
        break
    iteration_time += 1

# record file names
files = {
    'contracts': os.path.join(csvs, 'contracts.csv'),
    'fund': os.path.join(csvs, 'funds.csv'),
    'saving': os.path.join(csvs, 'savings.csv'),
    'client': os.path.join(csvs, 'clients.csv'),
    'transaction': os.path.join(csvs, 'transactions.csv'),
    'beneficiary': os.path.join(csvs, 'beneficiaries.csv'),
    'participant': os.path.join(csvs, 'participants.csv')
}

# save tables into csv files
ia_scrap.save_table_into_csv(control_unit, tables, files)

# save csv files into db
# ia_scrap.save_csv_to_db(control_unit, files)
