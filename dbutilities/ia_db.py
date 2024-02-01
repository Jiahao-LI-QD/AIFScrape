# CURRENT SAVING TABLE CREATION
import csv

import pandas as pd


def save_saving(cursor, values):
    cursor.executemany("insert into Saving_Current values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'IA', getdate())", values)
    cursor.commit()


def save_client(cursor, values):
    cursor.executemany(
        "insert into Client_Current values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, 'IA', getdate())",
        values)
    cursor.commit()


def save_contract(cursor, values):
    cursor.executemany(
        "insert into Contract_Current values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'IA', getdate())",
        values)
    cursor.commit()


def save_transaction(cursor, values):
    cursor.executemany("insert into Transaction_Current values (?, ?, ?, ?, ?, ?, ?, 'IA', getdate())", values)
    cursor.commit()


def save_fund(cursor, values):
    cursor.executemany("insert into Fund_Current values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'IA', getdate())", values)
    cursor.commit()


def save_participant(cursor, values):
    cursor.executemany("insert into Participant_Current values (?, ?, ?, ?, 'IA', getdate())", values)
    cursor.commit()


def save_beneficiary(cursor, values):
    cursor.executemany("insert into Beneficiary_Current values (?, ?, ?, ?, ?, ?, ?, 'IA', getdate())", values)
    cursor.commit()


def save_saving_history(cursor, values):
    cursor.executemany("insert into Saving_History values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'IA', getdate())", values)
    cursor.commit()


def save_client_history(cursor, values):
    cursor.executemany(
        "insert into Client_History values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, 'IA', getdate())",
        values)
    cursor.commit()


def save_contract_history(cursor, values):
    cursor.executemany("insert into Contract_History values "
                       "(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, "
                       " 'IA', getdate())",
                       values)
    cursor.commit()


def save_transaction_history(cursor, values):
    cursor.executemany("insert into Transaction_History values (?, ?, ?, ?, ?, ?, ?, 'IA', getdate())", values)
    cursor.commit()


def save_fund_history(cursor, values):
    cursor.executemany("insert into Fund_History values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'IA', getdate())", values)
    cursor.commit()


def save_participant_history(cursor, values):
    cursor.executemany("insert into Participant_History values (?, ?, ?, ?, 'IA', getdate())", values)
    cursor.commit()


def save_beneficiary_history(cursor, values):
    cursor.executemany("insert into Beneficiary_History values (?, ?, ?, ?, ?, ?, ?, 'IA', getdate())", values)
    cursor.commit()


def delete_current_participant_beneficiary(cursor):
    cursor.execute("exec Delete_Current_Participant_Beneficiary")


def delete_current_contract(cursor):
    cursor.execute("exec Delete_Current_Contract")


def delete_current_fund_saving(cursor):
    cursor.execute("exec Delete_Current_Fund_Saving")


def delete_current_client(cursor):
    cursor.execute("exec Delete_Current_Client")


def delete_current_transaction(cursor):
    cursor.execute("exec Delete_Current_Transaction")


def save_data_into_db(db_cursor, file_name, db_method, batch_size):
    with open(file_name) as f:
        f.readline()  # skip the headers
        data = [tuple(line[1:]) for line in csv.reader(f)]
    # in case of large dataset

    for i in range(-(len(data) // -batch_size)):
        db_method(db_cursor, data[i * batch_size:(i + 1) * batch_size])


def read_clients(db_cursor):
    db_cursor.execute("SELECT * FROM Client_Current")


def save_recover(cursor, values):
    cursor.executemany("insert into Error_contract_number_History values (?, ?, 'IA', getdate())", values)
    cursor.commit()
