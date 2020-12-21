import pandas as pd
import numpy as np


def load_data():
    """
    Loads the data from the .csv file into a pandas DataFrame
    :return: the pandas DataFrame containing the data from the .csv file
    """
    data = pd.read_csv("..\docs\pokemon.csv")

    # Changes the two columns type1 and type2 into a single column containing both info
    data["type2"] = data["type2"].fillna("None")
    data["type"] = data["type1"] + "/" + data["type2"]

    # Removes weird string value from base_egg_steps column
    data = data.drop(data[data["capture_rate"] == "30 (Meteorite)255 (Core)"].index)
    data["capture_rate"] = pd.to_numeric(data["capture_rate"])

    # Removes values from base_egg_steps rows if Pokémon is legendary
    # data.loc[data["is_legendary"] == 1, "base_egg_steps"] = np.nan

    return data


def only_legendary():
    """
    Removes all rows from the dataset pertaining to non-legendary Pokémon
    :return: a Pandas DataFrame containing only data on legendary Pokémon
    """
    data = load_data()
    data_legendary = data[data["is_legendary"] == 1]
    return data_legendary


def no_legendary():
    """
    Removes all rows from the dataset pertaining to legendary Pokémon
    :return: a Pandas DataFrame containing only data on non-legendary Pokémon
    """
    data = load_data()
    data = data[data["is_legendary"] == 0]
    data_no_legendary = data[data["base_egg_steps"] < 15000]
    return data_no_legendary


def group_data_mean(data, group_by_var):
    """
    Groups the data by mean using the parameter group_by_var
    :param group_by_var: The variable which the data is grouped on
    :return: A pandas DataFrame of the original data, grouped on group_by_var
    """
    data_grouped = data.groupby(group_by_var, as_index=False).mean()
    return data_grouped
