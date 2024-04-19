import pandas as pd


def get_data(data_length, data_path):
    data = pd.read_csv(data_path)
    return data[:data_length]


def inspect_data(data):
    print(data)