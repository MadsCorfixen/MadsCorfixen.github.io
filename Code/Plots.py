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
    fig.update_yaxes(title="Count", range=(-0.5, 62.5))

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


def create_legend_violin_plot():
    normal_data = dm.load_data()
    legendary_data = dm.only_legendary()

    fig = go.Figure()

    fig.add_trace(go.Violin(
        x=normal_data["is_legendary"],
        y=normal_data["base_total"],
        name="Non-Legendary",
        line_color="black",
        fillcolor="green")
    )

    fig.add_trace(go.Violin(
        x=legendary_data["is_legendary"],
        y=legendary_data["base_total"],
        name="Legendary",
        line_color="black",
        fillcolor="blue")
    )

    fig.update_layout(
        annotations=[dict(text="<b>Choose Comparison", x=1.01, xref="paper", xanchor="left",
                          y=0.92, yref="paper", showarrow=False)],
        legend=dict(x=1.005, xanchor="left", y=1),
        updatemenus=[dict(
            direction="down", x=1.01, y=0.9, xanchor="left", type="buttons",
            buttons=[
                dict(
                    label="Base Total",
                    method="update",
                    args=[
                        {"y": [normal_data["base_total"], legendary_data["base_total"]]},
                        {"title.text": "Comparison of Base Total"}
                    ]
                ),
                dict(
                    label="Base Egg Steps",
                    method="update",
                    args=[
                        {"y": [normal_data["base_egg_steps"], legendary_data["base_egg_steps"]]},
                        {"title.text": "Comparison of Base Egg Steps"}
                    ]
                ),
                dict(
                    label="Capture Rate",
                    method="update",
                    args=[
                        {"y": [normal_data["capture_rate"], legendary_data["capture_rate"]]},
                        {"title.text": "Comparison of Capture Rate"}
                    ]
                )
            ]
        )],
        title="Comparison of Base Total",
        xaxis=dict(
            tickmode='array',
            tickvals=[0, 1],
            ticktext=["Non-Legendary", "Legendary"]
        )
    )

    save_plot(fig, "ViolinPlot")
