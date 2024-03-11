from dbutilities import save_to_db
from ia_selenium.ia_contract_list import click_contract_list
from utilities.companys import companies
from utilities.split_excel import read_excel, split_dataframe, split_select_by_company
from utilities.get_confs import get_confs
from utilities.save_csv import get_csv_file_names, save_table_into_csv
from utilities.tables_utilities import merge_tables
from utilities.thread_generator import contracts_restart, threads_handler

# {
#         'csvs': csvs,
#         'parameters': ia_parameters,
#         'control_unit': control_unit,
#         'maximum_iteration': maximum_iteration,
#         'contract_file': contract_file,
#         'date_today': date_today,
#         'threading_tables': threading_tables,
#         'thread_number': thread_number
#  }
confs = get_confs()

# split contract file into n part according to thread number
contract_files = split_select_by_company(confs)

# list for store threads
threads_list = {}
# store the current alive threads names
current_list = []

# for loop generate threads
start_index = threads_handler(confs, threads_list, current_list, confs['company'], contract_files)

# find the crashed thread
# 1. restart
# 2. find what left start again
while True:
    contracts_left = contracts_restart(confs, contract_files, current_list)
    if len(contracts_left) == 0:
        break
    contract_files = split_dataframe(contracts_left, confs['thread_number'])
    threads_handler(confs, threads_list, current_list, confs['company'], contract_files)

# merge tables from threads
tables = merge_tables(confs, confs['company'])

# record file names
files = get_csv_file_names(confs['csvs'], confs['company'])

# save tables into csv files
save_table_into_csv(confs['control_unit'], tables, files, confs['company'])

# save csv files into db
save_to_db.save_csv_to_db(confs, files, tables, confs['company'])

# request contract list for next time
if confs['company'] == companies['iA']:
    click_contract_list(confs)
