import os
import sys
import threading
from datetime import datetime

import pandas as pd

from ia_selenium import ia_scrap, keys
from ia_selenium.ia_scrap import get_control, driver_setup, ia_app, create_table, ia_threading, merge_tables, \
    save_contract_list
from ia_selenium.split_excel import split_excel

# ia_wd : chrome driver
# maximum_iteration: max iteration of scrap loop
# control_unit: get control unit for scrap
# ia_parameters: get parameters setting
# tables: information containers
# csvs: the file location


# csvs
# tables
# control_unit
# set up the control unit & recovery_file unit
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
confs = ia_scrap.ia_get_confs()

contract_files = split_excel(os.path.join(confs['parameters']['csv_path'], confs['parameters']['contracts'], confs['contract_file']),
                             os.path.join(confs['parameters']['csv_path'], confs['date_today']),
                             confs['thread_number'])

threads_list = []

for i in range(confs['thread_number']):
    thread_name = 'thread' + str(i)
    threads_list.append(threading.Thread(target=ia_threading,
                                         args=(confs, 'thread' + str(i), contract_files[i],)))

for t in threads_list:
    t.start()
for t in threads_list:
    t.join()

# merge tables from threads
tables = merge_tables(confs)

# record file names
files = ia_scrap.get_csv_file_names(confs['csvs'])

# save tables into csv files
ia_scrap.save_table_into_csv(confs['control_unit'], tables, files)

# save csv files into db
# ia_scrap.save_csv_to_db(confs['control_unit'], files, tables)

# request contract numbers
# ia_scrap.click_contract_list(confs)

