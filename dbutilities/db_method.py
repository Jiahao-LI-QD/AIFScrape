# CURRENT SAVING TABLE CREATION
import csv

import pandas as pd

from dbutilities import dbColumns


def parameter_len(columns):
    """
    This method returns a string that contains a comma-separated list of question marks,
    with each question mark representing a parameter in the columns list.
    :param columns: A list of column names.
    :return: A string that contains a comma-separated list of question marks,
             with each question mark representing a parameter in the columns list.
    """
    return '?, ' * len(columns)


def save_saving(cursor, values, company):
    """
    This function is used to save a list of values into a database table named "Saving_Current".
    :param cursor: A database cursor object used to execute SQL statements.
    :param values: A list of tuples representing the values to be inserted into the "Saving_Current" table.
                   Each tuple should contain the values for each column in the table.
    :param company: A string representing the name of the company.
    :return: Nothing return. It saves the provided values into the "Saving_Current" table in the database.
    """
    cursor.executemany("insert into Saving_Current values (" + parameter_len(dbColumns.saving_columns) +
                       "getdate())", values)
    cursor.commit()


def save_client(cursor, values):
    """
    This method is used to insert multiple rows of data into the "Client_Current" table in a database.
    :param cursor: A cursor object that allows interaction with the database.
    :param values: A list of tuples, where each tuple represents a row of data to be inserted into
                   the "Client_Current" table.
    :return: Nothing return. It inserts the rows of data into the "Client_Current" table in the database.
    """
    cursor.executemany("insert into Client_Current values (" + parameter_len(dbColumns.client_columns) +
                       "getdate())", values)
    cursor.commit()


def save_contract(cursor, values):
    """
    This method is used to insert multiple rows of data into the "Contract_Current" table in a database.
    :param cursor: A cursor object that allows interaction with the database.
    :param values: A list of tuples, where each tuple represents a row of data to be inserted into the table.
    :return: Nothing return. It inserts the provided values into the "Contract_Current" table in the database.
    """
    cursor.executemany("insert into Contract_Current values (" + parameter_len(dbColumns.contract_columns) +
                       "getdate())", values)
    cursor.commit()


def save_transaction(cursor, values):
    """
    This method is used to insert multiple rows of transaction data into a database table.
    :param cursor: A cursor object used to execute SQL statements.
    :param values: A list of tuples, where each tuple represents a row of transaction data.
    :return: Nothing return. It inserts the provided values into the "Transaction_Current" table in the database.
    """
    cursor.executemany("insert into Transaction_Current values (" + parameter_len(dbColumns.transaction_columns) +
                       "getdate())", values)
    cursor.commit()


def save_fund(cursor, values):
    """
    This method is used to insert multiple rows of data into the "Fund_Current" table in a database.
    :param cursor: A cursor object that allows interaction with the database.
    :param values:  A list of tuples, where each tuple represents a row of data to be inserted into
                    the "Fund_Current" table. Each tuple should contain the values for the columns in the table.
    :return: Nothing return. The rows of data are inserted into the "Fund_Current" table in the database.
    """
    cursor.executemany("insert into Fund_Current values (" + parameter_len(dbColumns.fund_columns) +
                       "getdate())", values)
    cursor.commit()


def save_participant(cursor, values):
    """
    This method is used to insert multiple rows of data into the "Participant_Current" table in a database.
    :param cursor: A database cursor object.
    :param values: A list of rows to be inserted into the "Participant_Current" table. Each row should be
                   a tuple or list containing the values for each column in the table.
    :return: Nothing return.  It inserts the rows specified in the values parameter into the
                              "Participant_Current" table in the database.
    """
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
    cursor.execute(f"exec Delete_Current_Participant_Beneficiary {company}")


def delete_current_contract(cursor, company):
    cursor.execute(f"exec Delete_Current_Contract {company}")


def delete_current_fund_saving(cursor, company):
    cursor.execute(f"exec Delete_Current_Fund_Saving {company}")


def delete_current_client(cursor, company):
    cursor.execute(f"exec Delete_Current_Client {company}")


def delete_current_transaction(cursor, company):
    cursor.execute(f"exec Delete_Current_Transaction {company}")


def save_data_into_db(db_cursor, file_name, db_method, batch_size):
    with open(file_name) as f:
        f.readline()  # skip the headers
        data = [tuple(line[1:]) for line in csv.reader(f)]
    # in case of large dataset

    for i in range(-(len(data) // -batch_size)):
        db_method(db_cursor, data[i * batch_size:(i + 1) * batch_size])


def read_clients(db_cursor):
    db_cursor.execute("SELECT * FROM Client_Current")


def save_recover(cursor, company, values):
    cursor.executemany("insert into Error_contract_number_History values (?, ?, " + company + ", getdate())", values)
    cursor.commit()
