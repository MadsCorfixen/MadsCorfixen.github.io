import numpy as np
import DataManipulation as dm
import plotly.graph_objects as go


def best_fit_linear(x_var, y_var):
    # y = a * x + b
    all_data = dm.load_data()
    data = dm.group_data_mean(all_data, "base_total")

    x = data[x_var]
    y = data[y_var]

    beta_1, beta_0 = np.polyfit(x, y, 1)

    x_plot = np.arange(0, max(x))
    y_plot = beta_1 * x_plot + beta_0

    trendline = go.Scatter(x=x_plot, y=y_plot)

    return trendline


def best_fit_exp(x_var, y_var):
    # y = a * e^(bx)
    all_data = dm.load_data()
    data = dm.group_data_mean(all_data, "base_total")

    x = data[x_var]
    y = data[y_var]

    slope, exponent = np.polyfit(x, np.log(y), 1, w=np.sqrt(y))

    x_plot = np.arange(0, max(x))
    y_plot = slope * np.exp(exponent * x_plot)

    trendline = go.Scatter(x=x_plot, y=y_plot)

    return trendline


def best_fit_log(x_var, y_var):
    # y = a + b * log(x)
    all_data = dm.load_data()
    data = dm.group_data_mean(all_data, "base_total")

    x = data[x_var]
    y = data[y_var]

    beta_0, beta_1 = np.polyfit(np.log(x), y, 1)

    x_plot = np.arange(0, max(x))
    y_plot = beta_0 + beta_1 * np.log(x_plot)

    trendline = go.Scatter(x=x_plot, y=y_plot)

    return trendline


