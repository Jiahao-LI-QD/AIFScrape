from utilities.search_traverse import scrape_traverse
from utilities.tables_utilities import create_table


def thread_generator(confs, thread_name, company, contract_file):
    # start the ia company scrapy process

    # create dataframes for all the tables
    # and get contract numbers for ia company
    tables = create_table(contract_file, company, True)
    # do - while loop to traverse through the contract numbers until no exception
    iteration_time = 0
    while iteration_time < confs['maximum_iteration']:
        scrape_traverse(confs, tables, iteration_time, company, thread_name)
        if len(tables['recover']) == 0:
            break
        iteration_time += 1

    tables['contracts'] = tables['contracts'][~tables['contracts']['Contract_number'].isin(tables['recover'])]
    confs['threading_tables'][thread_name] = tables
