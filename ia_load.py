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
