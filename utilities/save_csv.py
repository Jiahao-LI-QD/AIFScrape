import os
from datetime import datetime

from utilities.companys import companies


def save_table_into_csv(control_unit, tables, files, company):
    """
    This method saves different tables into CSV files based on the value of control_unit and the specified company.
    :param control_unit: an integer of the control mode. Each mode corresponds to a specific table to be saved.
    :param tables: a dictionary containing the tables to be saved.
                   The keys are the table names and the values are the table data.
    :param files: a dictionary containing the file names for each table to be saved.
                  The keys are the table names and the values are the file names.
    :param company: a string representing the company name.
    :return: nothing return, but new csv files of dataframe scraped from website saved.
    """
    print("Saving to CSVS")
    if control_unit & 1:
        tables['fund'].to_csv(files['fund'])
        if company == companies['iA']:
            tables['saving'].to_csv(files['saving'])
    if control_unit & 2:
        tables['transaction'].to_csv(files['transaction'])
    if control_unit & 4:
        tables['client'].to_csv(files['client'])
        tables['beneficiary'].to_csv(files['beneficiary'])
        tables['participant'].to_csv(files['participant'])
    tables['contracts'].to_csv(files['contracts'])

    print(f"{datetime.now()}: CSVs saved!")
    print("=========================")


def get_csv_file_names(path, company):
    """
    This method returns a dictionary that maps specific file names to their corresponding paths.
    :param path: (string) The path to the directory where the CSV files are located.
    :return: the dictionary mapping file names to their paths.
    """
    return {
        # The full path is obtained by joining the path with the specific file name
        'contracts': os.path.join(path, company + '_contracts.csv'),
        'fund': os.path.join(path, company + '_funds.csv'),
        'saving': os.path.join(path, company + '_savings.csv'),
        'client': os.path.join(path, company + '_clients.csv'),
        'transaction': os.path.join(path, company + '_transactions.csv'),
        'beneficiary': os.path.join(path, company + '_beneficiaries.csv'),
        'participant': os.path.join(path, company + '_participants.csv')
    }
