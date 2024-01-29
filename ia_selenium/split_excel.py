import pandas as pd


# function for loading excels into pd dataframe and splitting them into equal parts of parameter value.
# file_path is the read_excel file path, folder_path is the folder we save the excels into.
def split_excel(file_path, folder_path, num_chunks):
    df = pd.read_excel(file_path).iloc[2:]
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

    for i in range(len(parts)):
        file_name = '\contract_part_' + str(i + 1) + '.xlsx'
        full_path = folder_path + file_name
        parts[i].to_excel(full_path, index=False)

path = "D:\ia_csvs\contracts\contracts_final_1.XLSX"
folder = "D:\ia_csvs\contracts"
split_excel(path, folder,4)
