import numpy as np
import plotly.graph_objects as go


def best_fit_linear(data, x_var, y_var, color):
    """
    Determines the linear line of best fit between x_var and y_var for the inputted data.
    :param data: The data of which to find the line of best fit
    :param x_var: The dependent variable to use in the regression
    :param y_var: The response variable to use in the regression
    :param color: The desired color of the line of best fit
    :return: An object of the go.Figure type, containing the line of best fit
    """
    # y = a * x + b
    x = data[x_var]
    y = data[y_var]

    beta_1, beta_0 = np.polyfit(x, y, 1)

    x_plot = np.arange(min(x), max(x))
    y_plot = beta_1 * x_plot + beta_0

    trendline = go.Scatter(x=x_plot, y=y_plot, line=dict(color=color), showlegend=False, visible=False)
    return trendline, y, y_plot


def best_fit_exp(data, x_var, y_var, color):
    """
    Determines the exponential line of best fit between x_var and y_var for the inputted data.
    :param data: The data of which to find the line of best fit
    :param x_var: The dependent variable to use in the regression
    :param y_var: The response variable to use in the regression
    :param color: The desired color of the line of best fit
    :return: An object of the go.Figure type, containing the line of best fit
    """
    # y = a * e^(bx)
    x = data[x_var]
    y = data[y_var]

    beta_0, beta_1 = np.polyfit(x, np.log(y), 1, w=np.sqrt(y))

    x_plot = np.arange(min(x), max(x))
    y_plot = np.exp(beta_1) * np.exp(beta_0*x_plot)

    trendline = go.Scatter(x=x_plot, y=y_plot, line=dict(color=color), showlegend=False, visible=False)
    return trendline, y, y_plot


def best_fit_log(data, x_var, y_var, color):
    """
    Determines the logarithmic line of best fit between x_var and y_var for the inputted data.
    :param data: The data of which to find the line of best fit
    :param x_var: The dependent variable to use in the regression
    :param y_var: The response variable to use in the regression
    :param color: The desired color of the line of best fit
    :return: An object of the go.Figure type, containing the line of best fit
    """
    # y = a + b * log(x)
    x = data[x_var]
    y = data[y_var]

    beta_0, beta_1 = np.polyfit(np.log(x), y, 1)

    x_plot = np.arange(min(x), max(x))
    y_plot = beta_1 + beta_0 * np.log(x_plot)

    trendline = go.Scatter(x=x_plot, y=y_plot, line=dict(color=color), showlegend=False, visible=False)
    return trendline, y, y_plot


def get_r_squared(y_obs, y_pred):
    """
    Determines the correlation coefficient for a line of best fit.
    :param y_obs: The observed values for the response variable.
    :param y_pred: The predicted values for the response variable.
    :return: The correlation coefficient (R squared)
    """
    y_mean = y_obs.mean()

    ss_total = 0
    ss_residual = 0

    for i in range(0, len(y_obs)):
        ss_total = ss_total + (y_obs[i] - y_mean)**2

    for i in range(0, len(y_obs)):
        ss_residual = ss_residual + (y_obs[i] - y_pred[i])**2

    r = 1 - ss_residual / ss_total
    r_squared = r**2

    return r_squared
