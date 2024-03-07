import os
import pandas as pd

from cl_selenium.cl_policies import get_serial_number
from dbutilities import dbColumns
from eq_selenium.eq_policies import get_policies
from utilities.companys import companies
from utilities.dataframe_format import adjust_dataframe


def read_excel(file_path, folder_path, num_chunks):
    """
    defines a function named split_excel that takes in a file path, a folder path, and the number of chunks as inputs.
    The function reads an Excel file, drops the first two rows, renames the columns, removes duplicate rows based on a
    specific column, and then splits the remaining data into smaller chunks. The function saves each chunk as a separate
    Excel file in the specified folder path and returns a list of the file paths.

    :param file_path: The path of the Excel file to be split loaded from ia_conf.
    :param folder_path: The path of the folder where the split Excel files will be saved,
                        default is the generated folder.
    :param num_chunks: The number of smaller chunks to split the data into, defined by input parameters in ia_app.py.
    :return: file_paths (list): A list of file paths where the split Excel files are saved.

    Workflow:
    1. Read Excel File
    2. Remove header rows and rename columns to fit db.
    3. Remove duplicates contract numbers.
    4. Split into smaller parts.
    5. Calculate chunk size.
    6. Save as separate Excel files.
    """
    df = pd.read_excel(file_path, dtype=str).iloc[2:]
    df['Company'] = companies['iA']
    df.columns = dbColumns.contract_columns
    df = df.drop_duplicates(subset=['Contract_number'])

    split_dfs = split_dataframe(df, num_chunks)
    file_paths = []

    for i in range(len(split_dfs)):
        file_name = 'contract_part_' + str(i + 1) + '.xlsx'
        full_path = os.path.join(folder_path, file_name)
        file_paths.append(full_path)
        split_dfs[i].to_excel(full_path, index=False)

    return split_dfs


def split_dataframe(df, num_chunks):
    """
    splits the DataFrame into smaller parts based on the specified number of chunks and returns a list of the split DataFrames.
    :param df: The DataFrame to be split into smaller parts.
    :param num_chunks: The number of smaller parts to split the DataFrame into.
    :return: A list of DataFrames, each representing a split part of the original DataFrame.

    Workflow:
    1. Calculate the number of rows in the DataFrame and the size of each part.
    2. Calculate the remainder row by taking the modulo of the number of rows and the number of chunks.
    3. Initialize an empty list to store the split DataFrames.
    4. Iterate over the number of chunks: Slice the DataFrame to extract the current start index and end index,
                                            append the current part to the list of split DataFrames.
    5. If there is a remainder row, concatenate the last part with the remaining rows from the original DataFrame.
    6. Return the list of split DataFrames.
    """
    num_rows = len(df)
    parts_size = (num_rows // num_chunks)
    remainder_row = num_rows % num_chunks
    parts = []

    # separate the big dataframe into num_chunks amount of smaller dfs
    for i in range(num_chunks):
        start_index = i * parts_size
        end_index = min((i + 1) * parts_size, num_rows)
        df_part = df[start_index:end_index]
        parts.append(df_part)

    if remainder_row != 0:
        last_df = pd.concat([parts[-1], df[(-remainder_row):]])
        parts[-1] = last_df

    return parts


def split_select_by_company(confs):
    contracts = pd.DataFrame()

    match confs['company']:
        case 'iA':
            contracts = read_excel(confs['contract_path'],
                                   confs['csvs'],
                                   confs['thread_number'])
        case 'CL':
            # get dataframe with policies
            policies = get_serial_number(confs)

            # adjust dataframe format to fit iA contracts Excel.
            policies = adjust_dataframe(policies)

            # split contract file into n part according to thread number
            contracts = split_dataframe(policies, confs['thread_number'])
        case 'EQ':
            contracts = get_policies(confs)
        case _:
            # This case should never be taken
            print('Invalid company is taken. Will Exit!')
            exit()
    return contracts
