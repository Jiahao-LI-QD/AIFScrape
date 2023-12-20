from dbutilities import dbColumns, dbtemplate
from test import sample_csv
import faker
import random
from datetime import date

# sample_csv.random_data_generator(dbColumns.high_interest_columns,
#                                  dbtemplate.hi_template,
#                                  size=10001)
fake = faker.Faker()
Sex = ["Male", "Female", "Other"]
start_date = date(year=1950, month=1, day=1)
print(dbtemplate.contract_template)
