import pandas as pd


def load_data():
    data = pd.read_csv("..\docs\pokemon.csv")
    data["type2"] = data["type2"].fillna("None")
    data["type"] = data["type1"] + "/" + data["type2"]
    return data


def is_legendary(data):
    pass


