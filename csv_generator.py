from dbutilities import dbColumns, dbtemplate
from test import sample_csv

sample_csv.random_data_generator(dbColumns.high_interest_columns,
                                 dbtemplate.hi_template,
                                 size=10001)

