import threading

from ia_selenium import ia_scrap
from ia_selenium.ia_contract_list import click_contract_list
from utilities.companys import companies
from utilities.split_excel import read_excel
from utilities.get_confs import get_confs
from utilities.save_csv import get_csv_file_names, save_table_into_csv
from utilities.tables_utilities import merge_tables
from utilities.thread_generator import thread_generator

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
confs = get_confs(companies['iA'])

# split contract file into n part according to thread number
contract_files = read_excel(confs['contract_path'],
                            confs['csvs'],
                            confs['thread_number'])

# # list for store threads
# threads_list = []
#
# # for loop generate threads
# for i in range(confs['thread_number']):
#     thread_name = 'thread' + str(i)
#     threads_list.append(threading.Thread(target=thread_generator,
#                                          args=(confs, 'thread' + str(i), companies['iA'], contract_files[i],)))
#
# # start and join threads
# for t in threads_list:
#     t.start()
# for t in threads_list:
#     t.join()
#
# # merge tables from threads
# tables = merge_tables(confs, companies['iA'])
#
# # record file names
# files = get_csv_file_names(confs['csvs'], companies['iA'])
#
# # save tables into csv files
# save_table_into_csv(confs['control_unit'], tables, files, companies['iA'])
#
# # save csv files into db
# ia_scrap.save_csv_to_db(confs['control_unit'], files, tables, companies['iA'])

# request contract list for next time
# click_contract_list(confs)
