import threading
import time
from datetime import datetime

import pandas as pd

from dbutilities.dbColumns import contract_columns
from utilities.search_traverse import scrape_traverse
from utilities.tables_utilities import create_table


def thread_generator(confs, thread_name, company, contract_file):
    """
    The thread_generator function is responsible for generating threads to scrape data from different companies. It
    creates dataframes for different tables and retrieves contract numbers for the specified company. It then
    iterates through the contract numbers, calling the scrape_traverse function to scrape data for each contract. The
    iteration continues until there are no exceptions or until the maximum number of iterations is reached.

    :param confs: Configuration dictionary
    :param thread_name: the name of this thread
    :param company: company name
    :param contract_file: the contract file used for traverse loop

    :return: Nothing returned
    """
    # start the ia company scrapy process
    print(f"{thread_name} - {datetime.now()}: Thread starts")
    # create dataframes for all the tables
    # and get contract numbers for ia company
    tables = create_table(contract_file, company, True)

    try:
        # do - while loop to traverse through the contract numbers until no exception
        iteration_time = 0
        while iteration_time < confs['maximum_iteration']:
            scrape_traverse(confs, tables, iteration_time, company, thread_name)
            if len(tables['recover']) == 0:
                break
            iteration_time += 1
    except Exception as e:
        print(e)
        confs['thread_status'][thread_name] = False
    else:
        # keep only contracts that doesn't have contracts
        tables['contracts'] = tables['contracts'][~tables['contracts']['Contract_number'].isin(tables['recover'])]
        confs['thread_tables'][thread_name] = tables
        confs['thread_status'][thread_name] = True


def contracts_restart(confs, contract_files, current_list):
    contracts = pd.DataFrame(columns=contract_columns)

    for i in range(len(current_list)):
        name = current_list[i]
        if name not in confs['thread_status'] or not confs['thread_status'][name]:
            contracts = pd.concat([contracts, contract_files[i]], axis=0)
            print(name + ' is terminated abnormally. Will restart new threads')
    return contracts


def threads_handler(confs, threads_list, current_list, companies_name, contract_files):
    start_index = len(threads_list)
    current_list.clear()

    for i in range(start_index, start_index + confs['thread_number']):
        thread_name = 'thread' + str(i)
        current_list.append(thread_name)
        threads_list[thread_name] = threading.Thread(target=thread_generator,
                                                     args=(
                                                         confs, thread_name, companies_name, contract_files[i - start_index],))

    # start and join threads
    for t in current_list:
        threads_list[t].start()
        time.sleep(10)

    for t in current_list:
        threads_list[t].join()


