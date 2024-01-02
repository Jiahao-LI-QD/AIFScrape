from dbutilities import connection
import csv
from dbutilities import ia_db


def save_data_into_db(db_cursor, file_name, db_method, batch_size):
    with open(file_name) as f:
        f.readline()  # skip the headers
        data = [tuple(line[1:]) for line in csv.reader(f)]
    # in case of large dataset

    for i in range(-(len(data) // -batch_size)):
        db_method(db_cursor, data[i * batch_size:(i + 1) * batch_size])


try:
    cursor = connection.connect_db().cursor()
except Exception as e:
    print(e)
    print("Database connection failed!")
else:
    print("Database connection successful!")
    size = 1000
    save_data_into_db(cursor, "csvs/clients.csv", ia_db.save_client_history, size)
    save_data_into_db(cursor, "csvs/contracts.csv", ia_db.save_contract_history, size)
    save_data_into_db(cursor, "csvs/transactions.csv", ia_db.save_transaction_history, size)