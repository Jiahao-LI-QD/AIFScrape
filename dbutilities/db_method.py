# CURRENT SAVING TABLE CREATION
import csv

import pandas as pd

from dbutilities import dbColumns


def parameter_len(columns):
    return '?, ' * len(columns)


def save_saving(cursor, values, company):
    cursor.executemany("insert into Saving_Current values (" + parameter_len(dbColumns.saving_columns) +
                       "getdate())", values)
    cursor.commit()


def save_client(cursor, values):
    cursor.executemany("insert into Client_Current values (" + parameter_len(dbColumns.client_columns) +
                       "getdate())", values)
    cursor.commit()


def save_contract(cursor, values):
    cursor.executemany("insert into Contract_Current values (" + parameter_len(dbColumns.contract_columns) +
                       "getdate())", values)
    cursor.commit()


def save_transaction(cursor, values):
    cursor.executemany("insert into Transaction_Current values (" + parameter_len(dbColumns.transaction_columns) +
                       "getdate())", values)
    cursor.commit()


def save_fund(cursor, values):
    cursor.executemany("insert into Fund_Current values (" + parameter_len(dbColumns.fund_columns) +
                       "getdate())", values)
    cursor.commit()


def save_participant(cursor, values):
    cursor.executemany("insert into Participant_Current values (" + parameter_len(dbColumns.participant_columns) +
                       "getdate())", values)
    cursor.commit()


def save_beneficiary(cursor, values):
    cursor.executemany("insert into Beneficiary_Current values (" + parameter_len(dbColumns.beneficiary_columns) +
                       "getdate())", values)
    cursor.commit()


def save_saving_history(cursor, values):
    cursor.executemany("insert into Saving_History values (" + parameter_len(dbColumns.saving_columns) +
                       "getdate())", values)
    cursor.commit()


def save_client_history(cursor, values):
    cursor.executemany("insert into Client_History values (" + parameter_len(dbColumns.client_columns) +
                       "getdate())", values)
    cursor.commit()


def save_contract_history(cursor, values):
    cursor.executemany("insert into Contract_History values (" + parameter_len(dbColumns.contract_columns) +
                       "getdate())", values)
    cursor.commit()


def save_transaction_history(cursor, values):
    cursor.executemany("insert into Transaction_History values (" + parameter_len(dbColumns.transaction_columns) +
                       "getdate())", values)
    cursor.commit()


def save_fund_history(cursor, values):
    cursor.executemany("insert into Fund_History values (" + parameter_len(dbColumns.fund_columns) +
                       "getdate())", values)
    cursor.commit()


def save_participant_history(cursor, values):
    cursor.executemany("insert into Participant_History values (" + parameter_len(dbColumns.participant_columns) +
                       "getdate())", values)
    cursor.commit()


def save_beneficiary_history(cursor, values):
    cursor.executemany("insert into Beneficiary_History values (" + parameter_len(dbColumns.beneficiary_columns) +
                       "getdate())", values)
    cursor.commit()


def delete_current_participant_beneficiary(cursor, company):
    """
   executes a SQL query to delete the current beneficiary for the specified company.
    :param cursor:a database cursor object used to execute SQL queries.
    :param company:The name of the company for which the current beneficiary needs to be deleted.
    :return:no return,execute SQL queries.
    """
    cursor.execute(f"exec Delete_Current_Participant_Beneficiary {company}")


def delete_current_contract(cursor, company):
    """
    executes a SQL query to delete the current contract for the specified company.
    :param cursor:a database cursor object used to execute SQL queries.
    :param company:The name of the company for which the current contract needs to be deleted.
    :return:no return,execute SQL queries.
    """
    cursor.execute(f"exec Delete_Current_Contract {company}")


def delete_current_fund_saving(cursor, company):
    """
    executes an SQL query to delete the current fund for the specified company.
    :param cursor:a database cursor object used to execute SQL queries.
    :param company:The name of the company for which the current fund needs to be deleted.
    :return:no return,execute SQL queries.
    """
    cursor.execute(f"exec Delete_Current_Fund_Saving {company}")


def delete_current_client(cursor, company):
    """
    executes an SQL query to delete the current client for the specified company.
    :param cursor: a database cursor object used to execute SQL queries.
    :param company:The name of the company for which the current client needs to be deleted.
    :return:no return,execute SQL queries.
    """
    cursor.execute(f"exec Delete_Current_Client {company}")


def delete_current_transaction(cursor, company):
    """
    executes an SQL query to delete a current transaction for a given company in a database.
    :param cursor: a database cursor object used to execute SQL queries.
    :param company: The name of the company for which the current transaction needs to be deleted.
    :return:no return,execute SQL queries.
    """
    cursor.execute(f"exec Delete_Current_Transaction {company}")


def save_data_into_db(db_cursor, file_name, db_method, batch_size):
    """

    :param db_cursor: The database cursor object used to execute database queries.
    :param file_name: The name of the CSV file containing the data to be saved into the database
    :param db_method: The method used to save the data into the database.
    :param batch_size: The number of records to be processed in each batch.
    :return:no return, saving the data from the CSV file into the database using the provided db_method.
    Workflow:
    1.Open the specified CSV file.
    2.Skip the headers line in the file.
    3.Read the remaining lines in the file and convert each line into a tuple.
    4.Store the tuples in a list called data.
    5.Iterate over the data list in batches of size batch_size.
    6.Call the provided db_method with the current batch of data and the db_cursor to save the batch into the database.
    """
    with open(file_name) as f:
        f.readline()  # skip the headers
        data = [tuple(line[1:]) for line in csv.reader(f)]
    # in case of large dataset

    for i in range(-(len(data) // -batch_size)):
        db_method(db_cursor, data[i * batch_size:(i + 1) * batch_size])


def read_clients(db_cursor):
    """
     The function executes a SQL query to select all rows from a table named Client_Current.
    :param db_cursor:  a database cursor object that is used to execute the SQL query.
    :return:no return,executes a SQL statement using the executemany method to select all rows from a table named Client_Current.
    """
    db_cursor.execute("SELECT * FROM Client_Current")


def save_recover(cursor, company, values):
    """
    The function will execute the SQL statement to insert the values
    into the table and commit the changes to the database.

    :param cursor:  A cursor object used to execute SQL statements.
    :param company: A string representing the name of the company.
    :param values: A list of tuples containing the data to be inserted into the table.
    :return: no return,executes a SQL statement using the executemany method to insert the values into the table.
    """
    cursor.executemany("insert into Error_contract_number_History values (?, ?, " + company + ", getdate())", values)
    cursor.commit()
