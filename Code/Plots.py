import plotly.graph_objects as go
import DataManipulation as dm


def save_plot(fig, plot_name):
    save_directory = "../docs/UsedPlots/{}.html".format(plot_name)
    fig.write_html(save_directory)


def create_type_histogram():
    all_data = dm.load_data()
    mono_type = dm.mono_type()
    dual_type = dm.dual_type()

    fig = go.Figure()

    fig.add_trace(go.Histogram(x=all_data["type"], name="All Pokémon"))

    fig.update_layout(
        annotations=[dict(text="<b>Choose Mono- or<br />Dual Typing</b>", x=1.01, xref="paper", xanchor="left",
                          y=1, yref="paper", showarrow=False)],
        updatemenus=[dict(
            direction="down", x=1.01, y=0.966, xanchor="left", type="buttons",
            buttons=[
                dict(
                    label="All Pokémon",
                    method="update",
                    args=[
                        {"x": [all_data["type"]]},
                        {"title.text": "Distribution of All Pokémon Types"},
                    ]
                ),
                dict(
                    label="Mono-Typed Pokémon",
                    method="update",
                    args=[
                        {"x": [mono_type["type"]]},
                        {"title.text": "Distribution of Mono-Typed Pokémon"}
                    ]
                ),
                dict(
                    label="Dual-Typed Pokémon",
                    method="update",
                    args=[
                        {"x": [dual_type["type"]]},
                        {"title.text": "Distribution of Dual-Typed Pokémon"}
                    ]
                )
            ]
        )
        ],
        title="Distribution of All Pokémon Types",
    )

    fig.update_xaxes(categoryorder="total descending", title="Typing", range=(-0.5, 17.5))
    fig.update_yaxes(title="Count")

    save_plot(fig, "TypeHistogram")


def create_scatter_with_stats():
    data = dm.group_data_mean("type")
    x_var = "capture_rate"
    y_var = "base_egg_steps"
    colour_by = "base_total"

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

    save_plot(fig, "CorrelationPlot")


def violin_plot_type(normal_data, legendary_data):
    fig = go.Figure()

    fig.add_trace(go.Violin(
        x=normal_data["is_legendary"],
        y=normal_data["base_total"])
    )

    fig.add_trace(go.Violin(
        x=legendary_data["is_legendary"],
        y=legendary_data["base_total"])
    )

    fig.show()

