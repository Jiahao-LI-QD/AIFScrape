import pandas as pd

from dbutilities import dbColumns


def create_table(file_path, company_name, thread=False):
    """
    creating empty dataframes for different tables and initializing an empty list.
    It also reads contract numbers from an Excel file if the thread parameter is True.

    :param company_name: the company name for the tables
    :param file_path: The path to the Excel file containing contract numbers.
    :param thread: A boolean flag indicating whether the function is being called in a threaded context. Default is False.
    :return: "contracts" table


    Flow:
    1.The function initializes an empty dictionary called result with keys representing different tables and the recover list.
    2.If thread is False, the function reads contract numbers from the Excel file specified by file_path and assigns it to the contracts variable.
    3.The function creates empty dataframes for different tables using the pd.DataFrame constructor and assigns them to the corresponding keys in the result dictionary.
    4.The contracts key in the result dictionary is assigned the value of contracts based on which company.
    5.The result dictionary is returned as the output of the function.
    """
    # create pointers
    result = {'saving': pd.DataFrame(columns=dbColumns.saving_columns),
              'fund': pd.DataFrame(columns=dbColumns.fund_columns),
              'transaction': pd.DataFrame(columns=dbColumns.transaction_columns),
              'beneficiary': pd.DataFrame(columns=dbColumns.beneficiary_columns),
              'participant': pd.DataFrame(columns=dbColumns.participant_columns),
              'client': pd.DataFrame(columns=dbColumns.client_columns),
              'recover': []}

    contracts = None
    match company_name:
        case 'ia':
            if thread:
                contracts = pd.read_excel(file_path)
                contracts.columns = dbColumns.contract_columns
            else:
                contracts = pd.DataFrame(columns=dbColumns.contract_columns)
        case 'cl':
            # TODO
            pass
        case _:
            print("Error: Company for table is not specified")
    # get contract numbers for ia company

    result['contracts'] = contracts
    return result


def merge_tables(confs, company):
    """
    The merge_tables function takes a dictionary of tables and a company name as inputs. It merges the tables from
    the dictionary into a single table and returns the merged table

    :param confs: The configuration generated at the start of the app.
    :param company: The name of the company for which the tables are being merged.

    :return: tables:A dictionary containing the merged tables. Each table is
    represented by a key-value pair, where the key is the table name and the value is a pandas DataFrame. The recover
    key in the dictionary contains a list of recover values.
    """
    tables = create_table(None, company)
    for o in confs['threading_tables'].values():
        tables['saving'] = pd.concat([tables['saving'], o['saving']], axis=0)
        tables['fund'] = pd.concat([tables['fund'], o['fund']], axis=0)
        tables['transaction'] = pd.concat([tables['transaction'], o['transaction']], axis=0)
        tables['beneficiary'] = pd.concat([tables['beneficiary'], o['beneficiary']], axis=0)
        tables['participant'] = pd.concat([tables['participant'], o['participant']], axis=0)
        tables['contracts'] = pd.concat([tables['contracts'], o['contracts']], axis=0)
        tables['client'] = pd.concat([tables['client'], o['client']], axis=0)
        tables['recover'].extend(o['recover'])
    return tables
