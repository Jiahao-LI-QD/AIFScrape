from dbutilities import dbColumns, dbtemplate
from test import sample_csv

sample_csv.random_data_generator(dbColumns.client_columns,
                                 dbtemplate.client_template,
                                 1000).to_csv('csvs/clients.csv')

sample_csv.random_data_generator(dbColumns.contract_columns,
                                 dbtemplate.contract_template,
                                 1000).to_csv('csvs/contracts.csv')

sample_csv.random_data_generator(dbColumns.saving_columns,
                                 dbtemplate.saving_template,
                                 1000).to_csv('csvs/savings.csv')

sample_csv.random_data_generator(dbColumns.fund_columns,
                                 dbtemplate.fund_template,
                                 1000).to_csv('csvs/funds.csv')


sample_csv.random_data_generator(dbColumns.transaction_columns,
                                 dbtemplate.transaction_template,
                                 1000).to_csv('csvs/transactions.csv')

sample_csv.random_data_generator(dbColumns.participant_columns,
                                 dbtemplate.participant_template,
                                 1000).to_csv('csvs/participants.csv')

sample_csv.random_data_generator(dbColumns.beneficiary_columns,
                                 dbtemplate.beneficiary_template,
                                 1000).to_csv('csvs/beneficiaries.csv')
