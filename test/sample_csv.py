import pandas as pd

def random_data_generator(record_columns, template, size):
    samples = pd.DataFrame(columns=record_columns)
    data = template(size)
    for i in range(size):
        samples.loc[len(samples)] = data[i]
    return samples
