import plotly.graph_objects as go


def save_plot(fig, plot_name):
    save_directory = "../docs/UsedPlots/{}.html".format(plot_name)
    fig.write_html(save_directory)


def create_type_histogram(data):
    fig = go.Figure(data=[go.Histogram(x=data.type, histnorm='probability')])

    fig.update_xaxes(categoryorder="total descending")
    fig.update_layout(title="Distribution of Pokémon Types", xaxis_title="Typing", yaxis_title="Proportion")

    save_plot(fig, "TypeHistogram")


def create_scatter_with_stats(data, x_var, y_var, colour_by, plot_number):
    fig = go.Figure(data=go.Scatter(x=data[x_var].astype(int),
                                    y=data[y_var].astype(int),
                                    mode='markers',
                                    marker=dict(size=16,
                                                color=data[colour_by],
                                                colorscale="Viridis",
                                                colorbar=dict(
                                                    title="{}".format(colour_by)
                                                ),
                                                showscale=True)
                                    )
                    )

    fig.update_layout(title="Correlation between {}, {}, and {}".format(x_var, y_var, colour_by),
                      xaxis_title="{}".format(x_var),
                      yaxis_title="{}".format(y_var))

    save_plot(fig, "CorrelationPlot{}".format(plot_number))
