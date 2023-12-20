import pandas as pd
from datetime import date
import random

"""
Record_Date
contract_number
account_type
investment_type
rate
balance
snapshot_time
"""
def random_data_generator(record_columns, template, size):
    samples = pd.DataFrame(columns=record_columns)
    for _ in range(size):
        samples.loc[len(samples)] = template
    return samples


high_interest_columns = ["Record_Date", "contract_number", "account_type", "investment_type", "rate", "balance"]
hi_template = [date.today(), "contr" + str(random.randint(1, 10000)), "TFSA", "HI",
                                     random.random() * 10, random.random() * 10000]
size = 10001

random_data_generator(high_interest_columns, hi_template, size).to_csv("../sample.csv")
