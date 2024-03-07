import threading

from cl_selenium.cl_policies import get_serial_number
from dbutilities.save_to_db import save_csv_to_db
from utilities.companys import companies
from utilities.dataframe_format import adjust_dataframe
from utilities.get_confs import get_confs
from utilities.save_csv import get_csv_file_names, save_table_into_csv
from utilities.split_excel import split_dataframe
from utilities.tables_utilities import merge_tables
from utilities.thread_generator import thread_generator

# {
#         'csvs': csvs,
#         'parameters': cl_parameters,
#         'control_unit': control_unit,
#         'maximum_iteration': maximum_iteration,
#         'contract_file': None,
#         'date_today': date_today,
#         'threading_tables': threading_tables,
#         'thread_number': thread_number
#  }
confs = get_confs()


# list for store threads
threads_list = []

# for loop generate threads
for i in range(confs['thread_number']):
    thread_name = 'thread' + str(i)
    threads_list.append(threading.Thread(target=thread_generator,
                                         args=(confs, 'Thread' + str(i), companies['CL'], split_policies[i],)))

# start and join threads
for t in threads_list:
    t.start()
for t in threads_list:
    t.join()

# merge tables from threads
tables = merge_tables(confs, companies['CL'])

# record file names
files = get_csv_file_names(confs['csvs'], companies['CL'])

# save tables into csv files
save_table_into_csv(confs['control_unit'], tables, files, companies['CL'])

# save csv files into db
save_csv_to_db(confs['control_unit'], files, tables, companies['CL'])
# 1 client duplication problem?
