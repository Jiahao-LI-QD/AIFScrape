import pandas as pd

from dbutilities.dbColumns import contract_columns


def adjust_dataframe(df):
    """
    fills the new DataFrame with values from the input DataFrame based on column mappings.
    :param df: original dataframe that needs to be adjusted to fit iA format
    :return: The adjusted DataFrame with specific columns filled with values from the input DataFrame.
    """
    # Create a new dataframe with the same columns as your existing dataframe
    num_rows = len(df.index)
    new_df = pd.DataFrame(index=range(num_rows), columns=contract_columns)

    # Fill the new dataframe with None values (or any other default values)
    new_df['Applicant_last_name'] = df['Name']
    new_df['Contract_number'] = df['policy_number']
    new_df['Product'] = df['fund_name']
    new_df['Type'] = df['account_type']
    new_df['Representative_name'] = df['advisor']

    return new_df


