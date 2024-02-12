import os
import pandas as pd

from dbutilities import dbColumns


def split_excel(file_path, folder_path, num_chunks):
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
    df = pd.read_excel(file_path).iloc[2:]
    df.columns = dbColumns.contract_columns
    df = df.drop_duplicates(subset=['Contract_number'])
    num_rows = len(df)
    parts_size = (num_rows // num_chunks)
    remainder_row = num_rows % num_chunks
    parts = []
    file_paths = []

    # separate the big dataframe into num_chunks amount of smaller dfs
    for i in range(num_chunks):
        start_index = i * parts_size
        end_index = min((i + 1) * parts_size, num_rows)
        df_part = df[start_index:end_index]
        parts.append(df_part)

    if remainder_row != 0:
        last_df = pd.concat([parts[-1], df[(-remainder_row):]])
        parts[-1] = last_df

    for i in range(len(parts)):
        file_name = 'contract_part_' + str(i + 1) + '.xlsx'
        full_path = os.path.join(folder_path, file_name)
        file_paths.append(full_path)
        print(full_path)
        parts[i].to_excel(full_path, index=False)
    return file_paths
