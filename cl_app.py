import threading

from cl_selenium.cl_policies import get_serial_number
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
confs = get_confs('CL')

# get dataframe with policies
policies = get_serial_number(confs)

# adjust dataframe format to fit iA contracts Excel.
policies = adjust_dataframe(policies)

# split contract file into n part according to thread number
split_policies = split_dataframe(policies, confs['thread_number'])

# 1. cl_threading
# 2. scrape_traverse for cl?

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
files = get_csv_file_names(confs['csvs'])

# save tables into csv files
save_table_into_csv(confs['control_unit'], tables, files, companies['CL'])

# save csv files into db
# TODO: save CL database
# 1 client duplication problem?

