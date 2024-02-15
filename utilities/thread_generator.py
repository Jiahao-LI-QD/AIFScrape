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

    # keep only contracts that doesn't have contracts
    tables['contracts'] = tables['contracts'][~tables['contracts']['Contract_number'].isin(tables['recover'])]
    confs['threading_tables'][thread_name] = tables
