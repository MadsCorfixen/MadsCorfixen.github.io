import pandas as pd


def load_data():
    data = pd.read_csv("..\docs\pokemon.csv")

    data["type2"] = data["type2"].fillna("none")
    data["type"] = data["type1"] + "/" + data["type2"]

    data = data.drop(data[data["capture_rate"] == "30 (Meteorite)255 (Core)"].index)
    data["capture_rate"] = pd.to_numeric(data["capture_rate"])

    return data


def mono_type():
    data = load_data()
    data = data[data["type2"] == "none"]
    data = data.reset_index()
    return data


def dual_type():
    data = load_data()
    data = data[data["type2"] != "none"]
    data = data.reset_index()
    return data


def only_legendary():
    data = load_data()
    data_legendary = data[data["is_legendary"] == 1]
    return data_legendary


def no_legendary():
    data = load_data()
    data = data[data["is_legendary"] == 0]
    data_no_legendary = data[data["base_egg_steps"] < 15000]
    return data_no_legendary


def group_data_mean(group_by_var):
    data = load_data()
    data_grouped = data.groupby(group_by_var, as_index=False).mean()
    return data_grouped
