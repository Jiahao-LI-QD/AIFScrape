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
record_columns = ["Record_Date", "contract_number", "account_type", "investment_type", "rate", "balance"]
samples = pd.DataFrame(columns=record_columns)

count = 0
for _ in range(10001):
    # df = pd.concat([pd.DataFrame([[date.today(), "contract" + str(random.randint(1,10000)), "TFSA", "HI", random.random() * 10, random.random() * 10000]],
    #                              columns=samples.columns), samples], ignore_index=True)
    samples.loc[len(samples)] = [date.today(), "contr" + str(random.randint(1,10000)), "TFSA", "HI", random.random() * 10, random.random() * 10000]
    count += 1

samples.to_csv("../sample.csv")