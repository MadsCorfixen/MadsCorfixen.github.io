import pandas as pd


def load_data():
    """
    Loads the .csv file containing the Pokémon data and stores it in a pandas Dataframe.
    :return: A pandas Dataframe containing the data.
    """
    data = pd.read_csv("..\docs\pokemon.csv")

    data["type2"] = data["type2"].fillna("none")
    data["type"] = data["type1"] + "/" + data["type2"]

    data = data.drop(data[data["capture_rate"] == "30 (Meteorite)255 (Core)"].index)
    data["capture_rate"] = pd.to_numeric(data["capture_rate"])

    return data


def mono_type():
    """
    Removes all Pokémon from the data which are not mono-typed.
    :return: A pandas Dataframe containing no Pokémon that are not mono-typed.
    """
    data = load_data()
    data = data[data["type2"] == "none"]
    data = data.reset_index()
    return data


def dual_type():
    """
    Removes all Pokémon from the data which are not dual-typed.
    :return: A pandas Dataframe containing no Pokémon that are not dual-typed.
    """
    data = load_data()
    data = data[data["type2"] != "none"]
    data = data[data["type2"] != "None"]
    data = data[data["type2"] != data["type1"]]
    data = data.reset_index()
    return data


def only_legendary():
    """
    Removes all Pokémon from the data which are not legendary.
    :return: A pandas Dataframe containing no Pokémon that are not legendary.
    """
    data = load_data()
    data_legendary = data[data["is_legendary"] != 0]
    return data_legendary


def no_legendary():
    """
    Removes all Pokémon from the data which are legendary.
    :return: A pandas Dataframe containing no Pokémon that are legendary.
    """
    data = load_data()
    data_no_legendary = data[data["is_legendary"] != 1]
    return data_no_legendary


def group_data_mean(data, group_by_var):
    """
    Aggregates the data using mean, grouping by the group_by_var variable.
    :param data: The data to be grouped.
    :param group_by_var: The variable to use for grouping.
    :return: A pandas Dataframe containing the data that has been grouped.
    """
    data_grouped = data.groupby(group_by_var, as_index=False).mean()
    return data_grouped
