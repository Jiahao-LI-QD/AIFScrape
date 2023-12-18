from dbutilities import connection
import csv
from dbutilities import ia_db

try:
    cursor = connection.connect_db().cursor()
except Exception as e:
    print(e)
    print("Database connection failed!")
else:
    print("Database connection successful!")
    with open('sample.csv') as f:
        f.readline()  # skip the headers
        data = [tuple(line[1:]) for line in csv.reader(f)]
    # in case of large dataset

    batch_size=10000
    for i in range(-(len(data) // -batch_size)):
        ia_db.save_hi(cursor, data[i * batch_size:(i + 1) * batch_size])

