import os
from datetime import datetime


def save_table_into_csv(control_unit, tables, files, company):
    print("Saving to CSVS")
    if control_unit & 1:
        tables['fund'].to_csv(files['fund'])
        if company == 'IA':
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


def get_csv_file_names(path):
    return {
        'contracts': os.path.join(path, 'ia_contracts.csv'),
        'fund': os.path.join(path, 'ia_funds.csv'),
        'saving': os.path.join(path, 'ia_savings.csv'),
        'client': os.path.join(path, 'ia_clients.csv'),
        'transaction': os.path.join(path, 'ia_transactions.csv'),
        'beneficiary': os.path.join(path, 'ia_beneficiaries.csv'),
        'participant': os.path.join(path, 'ia_participants.csv')
    }
