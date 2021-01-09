import plotly.express as px
from plotly.subplots import make_subplots
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

    fig.add_trace(go.Histogram(x=all_data["type"],
                               name="All Pokémon",
                               marker=dict(
                                   line=dict(
                                       width=1.5,
                                       color="black"
                                   ),
                                   color="green"
                               )
                               )
                  )

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
    all_data = dm.load_data()
    data = dm.group_data_mean(all_data, "type")
    x_var = "capture_rate"
    y_var = "base_egg_steps"
    colour_by = "base_total"

    fig = go.Figure(data=go.Scatter(x=data[x_var].astype(int),
                                    y=data[y_var].astype(int),
                                    mode='markers',
                                    marker=dict(size=16,
                                                color=data[colour_by],
                                                colorscale="Viridis",
                                                colorbar=dict(title="{}".format(colour_by)),
                                                showscale=True))
                    )

    fig.update_layout(title="Correlation between {}, {}, and {}".format(x_var, y_var, colour_by),
                      xaxis_title="{}".format(x_var),
                      yaxis_title="{}".format(y_var))

    fig.update_xaxes(range=(-5, 260))

    save_plot(fig, "CorrelationPlot")


def create_legend_violin_plot(show_points=True, add_sample_size=False, file_name="ViolinPlot"):
    normal_data = dm.no_legendary()
    legendary_data = dm.only_legendary()

    size_normal = len(normal_data)
    size_legend = len(legendary_data)

    if show_points:
        show_points = "all"

    if not add_sample_size:
        size_normal = None
        size_legend = None

    fig = go.Figure()

    fig.add_trace(go.Violin(
        x=normal_data["is_legendary"],
        y=normal_data["base_total"],
        name="Non-Legendary",
        line_color="black",
        fillcolor="green",
        points=show_points,
        jitter=0.25,
        marker=dict(
            color="green",
            opacity=0.25
        ))
    )

    fig.add_trace(go.Violin(
        x=legendary_data["is_legendary"],
        y=legendary_data["base_total"],
        name="Legendary",
        line_color="black",
        fillcolor="blue",
        points=show_points,
        jitter=0.25,
        marker=dict(
            color="blue",
            opacity=0.25
        ),
        scalemode="count")
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
                        {"yaxis.title.text": "Base Total"}
                    ]
                ),
                dict(
                    label="Base Egg Steps",
                    method="update",
                    args=[
                        {"y": [normal_data["base_egg_steps"], legendary_data["base_egg_steps"]]},
                        {"yaxis.title.text": "Base Egg Steps"}
                    ]
                ),
                dict(
                    label="Capture Rate",
                    method="update",
                    args=[
                        {"y": [normal_data["capture_rate"], legendary_data["capture_rate"]]},
                        {"yaxis.title.text": "Capture Rate"}
                    ]
                )
            ]
        )],
        xaxis=dict(
            tickmode='array',
            tickvals=[0, 1],
            ticktext=["Non-Legendary<br />Sample Size: {}".format(size_normal),
                      "Legendary<br />Sample Size: {}".format(size_legend)]
        )
    )

    fig.update_yaxes(rangemode="nonnegative", title="Base Total")
    fig.update_layout(title="Comparison of Attributes between Legendary and non-Legendary Pokémon")

    save_plot(fig, file_name)


def create_legend_boxplot():
    normal_data = dm.load_data()
    legendary_data = dm.only_legendary()

    fig = go.Figure()

    fig.add_trace(go.Box(x=normal_data["is_legendary"],
                         y=normal_data["base_total"],
                         name="Non-Legendary",
                         line_color="black",
                         fillcolor="green"))

    fig.add_trace(go.Box(x=legendary_data["is_legendary"],
                         y=legendary_data["base_total"],
                         name="Legendary",
                         line_color="black",
                         fillcolor="blue"))

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
                        {"yaxis.title.text": "Base Total"}
                    ]
                ),
                dict(
                    label="Base Egg Steps",
                    method="update",
                    args=[
                        {"y": [normal_data["base_egg_steps"], legendary_data["base_egg_steps"]]},
                        {"yaxis.title.text": "Base Egg Steps"}
                    ]
                ),
                dict(
                    label="Capture Rate",
                    method="update",
                    args=[
                        {"y": [normal_data["capture_rate"], legendary_data["capture_rate"]]},
                        {"yaxis.title.text": "Capture Rate"}
                    ]
                )
            ]
        )],
        xaxis=dict(
            tickmode='array',
            tickvals=[0, 1],
            ticktext=["Non-Legendary", "Legendary"]
        )
    )

    fig.update_yaxes(rangemode="nonnegative", title="Base Total")
    fig.update_layout(title="Comparison of Attributes between Legendary and non-Legendary Pokémon")

    save_plot(fig, "BoxPlot")


def linked_plot():
    all_data = dm.load_data()
    data = dm.group_data_mean(all_data, "base_total")

    legend_data = dm.only_legendary()
    legend_data = dm.group_data_mean(legend_data, "base_total")

    normal_data = dm.no_legendary()
    normal_data = dm.group_data_mean(normal_data, "base_total")

    mono_data = dm.mono_type()
    mono_data = dm.group_data_mean(mono_data, "base_total")

    dual_data = dm.dual_type()
    dual_data = dm.group_data_mean(dual_data, "base_total")

    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.02)

    fig.add_trace(
        go.Scatter(
            x=data["base_total"],
            y=data["base_egg_steps"],
            mode="markers",
            name="Base Egg Steps",
            marker=dict(
                size=12,
                color="green",
                line=dict(
                    color="black",
                    width=1.5
                )
            )
        ),
        row=1,
        col=1
    )

    fig.add_trace(
        go.Scatter(
            x=data["base_total"],
            y=data["capture_rate"],
            mode="markers",
            name="Capture Rate",
            marker=dict(
                size=12,
                color="blue",
                line=dict(
                    color="black",
                    width=1.5
                )
            )
        ),
        row=2,
        col=1
    )

    fig.update_layout(
        annotations=[dict(text="<b>Choose Pokémon Category", x=1.01, xref="paper", xanchor="left",
                          y=0.94, yref="paper", showarrow=False)],
        legend=dict(x=1.005, xanchor="left", y=1),
        updatemenus=[
            dict(direction="down",
                 x=1.01,
                 y=0.92,
                 xanchor="left",
                 buttons=list([
                     dict(label="All Pokémon",
                          method="update",
                          args=[
                              {"y": [data["base_egg_steps"], data["capture_rate"]]}
                          ]),
                     dict(label="Legendary Pokémon",
                          method="update",
                          args=[
                              {"y": [legend_data["base_egg_steps"], legend_data["capture_rate"]]}
                          ]),
                     dict(label="Non-Legendary Pokémon",
                          method="update",
                          args=[
                              {"y": [normal_data["base_egg_steps"], normal_data["capture_rate"]]}
                          ]),
                     dict(label="Mono-Typed Pokémon",
                          method="update",
                          args=[
                              {"y": [mono_data["base_egg_steps"], mono_data["capture_rate"]]}
                          ]),
                     dict(label="Dual-Typed Pokémon",
                          method="update",
                          args=[
                              {"y": [dual_data["base_egg_steps"], dual_data["capture_rate"]]}
                          ])
                     ]))])

    fig.update_xaxes(title_text="Base Total", row=2, col=1)
    fig.update_yaxes(title_text="Base Egg Steps", row=1, col=1)
    fig.update_yaxes(title_text="Capture Rate", row=2, col=1)

    save_plot(fig, "LinkedPlot")
