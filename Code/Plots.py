import plotly.graph_objects as go


def create_type_histogram(data):
    fig = go.Figure(data=[go.Histogram(x=data.type, histnorm='probability')])

    fig.update_xaxes(categoryorder="total descending")
    fig.update_layout(title="Distribution of Pokémon Types", xaxis_title="Typing", yaxis_title="Proportion")

    fig.write_html("../UsedPlots/TypeHistogram.html")
    fig.show()


def scatter_with_stats(data, x_var, y_var):
    pass
