import numpy as np
import DataManipulation as dm


def best_fit_linear(x_var, y_var, group_by):
    all_data = dm.load_data()
    data = dm.group_data_mean(all_data, group_by)

    x = data[x_var]
    y = data[y_var]

    slope, intercept = np.polyfit(x, y, 1)

    x_start = 0
    y_start = intercept
    x_end = data[x_var][-1]
    y_end = data[y_var][-1] * slope

    return x_start, y_start, x_end, y_end


def best_fit_exp():
    pass


def best_fit_log():
    pass
