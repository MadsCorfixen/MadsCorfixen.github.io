from plotly.subplots import make_subplots
import plotly.graph_objects as go
import DataManipulation as dm
import Regression as rgr


def save_plot(fig, plot_name):
    """
    This function is used to directly save the figure as an .html file, titled as plot_name
    :param fig: A variable of the go.Figure type containing the figure which is to be saved locally.
    :param plot_name: The wanted title of the .html file.
    """
    save_directory = "../docs/UsedPlots/{}.html".format(plot_name)
    fig.write_html(save_directory)


def create_type_histogram():
    """
    Creates a histogram which shows the distribution of mono- and dual-typed Pokémon. Also includes the option to
    show the distribution of all Pokémon at once, or only show mono-typed, or only show dual-typed.
    """
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
        annotations=[dict(text="<b>Show:</b>", x=1.01, xref="paper", xanchor="left",
                          y=1, yref="paper", showarrow=False)],
        updatemenus=[dict(
            direction="down", x=1.01, y=0.97, xanchor="left", type="buttons",
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
                    label="Only Mono-Typed Pokémon",
                    method="update",
                    args=[
                        {"x": [mono_type["type1"]]},
                        {"title.text": "Distribution of Mono-Typed Pokémon"}
                    ]
                ),
                dict(
                    label="Only Dual-Typed Pokémon",
                    method="update",
                    args=[
                        {"x": [dual_type["type"]]},
                        {"title.text": "Distribution of Dual-Typed Pokémon"}
                    ]
                )
            ]
        )
        ],
        title="Distribution of All Pokémon Types"
    )

    fig.update_xaxes(categoryorder="total descending", title="Typing", range=(-0.5, 17.5))
    fig.update_yaxes(title="Amount of Pokémon with Typing", range=(-0.5, 62.5))

    save_plot(fig, "TypeHistogramUpdated")


def create_scatter_with_stats():
    """
    Creates a scatter plot which tries to visualize correlation between capture rate, base egg steps, and base total
    of Pokémon. To use 3 variables in a 2-dimensional plot, the colour channel is utilized to signify base total.
    """
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
    fig.update_yaxes(range=(-1000, 35000))

    save_plot(fig, "CorrelationPlot")


def create_legend_violin_plot(show_points=True, add_sample_size=False, file_name="ViolinPlot"):
    normal_data = dm.no_legendary()
    legendary_data = dm.only_legendary()

    size_normal = len(normal_data)
    size_legend = len(legendary_data)

    fig = go.Figure()

    if show_points:
        show_points = "all"

    if add_sample_size:
        fig.update_layout(xaxis=dict(
            tickmode='array',
            tickvals=[0, 1],
            ticktext=["Non-Legendary<br />Sample Size: {}".format(size_normal),
                      "Legendary<br />Sample Size: {}".format(size_legend)]
        )
        )

    elif not add_sample_size:
        fig.update_layout(xaxis=dict(
            tickmode='array',
            tickvals=[0, 1],
            ticktext=["Non-Legendary",
                      "Legendary"]
        )
        )

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
        )]
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
        annotations=[dict(text="<b>Choose Comparison:", x=1.01, xref="paper", xanchor="left",
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
    opacity_value = 0.5

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
            ),
            opacity=opacity_value
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
            ),
            opacity=opacity_value
        ),
        row=2,
        col=1
    )

    linear_line_egg = rgr.best_fit_linear(data=data, x_var="base_total", y_var="base_egg_steps", color="green")
    linear_egg_r_squared = round(rgr.get_r_squared(linear_line_egg[1], linear_line_egg[2]),
                                 2)

    exponential_line_egg = rgr.best_fit_exp(data=data, x_var="base_total", y_var="base_egg_steps", color="green")
    exponential_egg_r_squared = round(rgr.get_r_squared(exponential_line_egg[1], exponential_line_egg[2]),
                                      2)

    logarithmic_line_egg = rgr.best_fit_log(data=data, x_var="base_total", y_var="base_egg_steps", color="green")
    logarithmic_egg_r_squared = round(rgr.get_r_squared(logarithmic_line_egg[1], logarithmic_line_egg[2]),
                                      2)

    linear_line_capture = rgr.best_fit_linear(data=data, x_var="base_total", y_var="capture_rate", color="blue")
    linear_capture_r_squared = round(rgr.get_r_squared(linear_line_capture[1], linear_line_capture[2]),
                                     2)

    exponential_line_capture = rgr.best_fit_exp(data=data, x_var="base_total", y_var="capture_rate", color="blue")
    exponential_capture_r_squared = round(rgr.get_r_squared(exponential_line_capture[1], exponential_line_capture[2]),
                                          2)

    logarithmic_line_capture = rgr.best_fit_log(data=data, x_var="base_total", y_var="capture_rate", color="blue")
    logarithmic_capture_r_squared = round(rgr.get_r_squared(logarithmic_line_capture[1], logarithmic_line_capture[2]),
                                          2)

    fig.add_trace(linear_line_egg[0], row=1, col=1)
    fig.add_trace(exponential_line_egg[0], row=1, col=1)
    fig.add_trace(logarithmic_line_egg[0], row=1, col=1)

    fig.add_trace(linear_line_capture[0], row=2, col=1)
    fig.add_trace(exponential_line_capture[0], row=2, col=1)
    fig.add_trace(logarithmic_line_capture[0], row=2, col=1)

    test_annotations = [
        dict(
            text="<b>Add or Remove Trendlines</b>",
            x=1.01, xref="paper",
            xanchor="left",
            y=0.95,
            yref="paper",
            showarrow=False)]

    linear_annotation = [
        dict(
            showarrow=True,
            x=779,
            y=12857.88,
            text="R&#178;: {}".format(linear_egg_r_squared),
            xref="x1",
            yref="y1",
            font=dict(
                family="Times New Roman",
                size=20,
                color="white"
            ),
            bordercolor='white',
            bgcolor='green'
        ),
        dict(
            showarrow=True,
            x=779,
            y=-43.56646,
            text="R&#178;: {}".format(linear_capture_r_squared),
            xref="x2",
            yref="y2",
            font=dict(
                family="Times New Roman",
                size=20,
                color="white"
            ),
            bordercolor='white',
            bgcolor='blue'
        )
    ]

    exponential_annotations = [
        dict(
            showarrow=True,
            x=779,
            y=20381.39,
            text="R&#178;: {}".format(exponential_egg_r_squared),
            xref="x1",
            yref="y1",
            font=dict(
                family="Times New Roman",
                size=20,
                color="white"
            ),
            bordercolor='white',
            bgcolor='green'
        ),
        dict(
            showarrow=True,
            x=779,
            y=24.12334,
            text="R&#178;: {}".format(exponential_capture_r_squared),
            xref="x2",
            yref="y2",
            font=dict(
                family="Times New Roman",
                size=20,
                color="white"
            ),
            bordercolor='white',
            bgcolor='blue'
        )
    ]

    logarithmic_annotations = [
        dict(
            showarrow=True,
            x=779,
            y=10257.68,
            text="R&#178;: {}".format(logarithmic_egg_r_squared),
            xref="x1",
            yref="y1",
            font=dict(
                family="Times New Roman",
                size=20,
                color="white"
            ),
            bordercolor='white',
            bgcolor='green'
        ),
        dict(
            showarrow=True,
            x=779,
            y=-4.222479,
            text="R&#178;: {}".format(logarithmic_capture_r_squared),
            xref="x2",
            yref="y2",
            font=dict(
                family="Times New Roman",
                size=20,
                color="white"
            ),
            bordercolor='white',
            bgcolor='blue'
        )
    ]

    fig.update_layout(updatemenus=[
            dict(
                type="buttons",
                direction="down",
                x=1.01,
                y=0.925,
                xanchor="left",
                showactive=True,
                buttons=[
                    dict(label="Click to Remove Trendlines",
                         method="update",
                         args=[
                             {"visible": [True, True, False, False, False, False, False, False]},
                             {"annotations": test_annotations}
                         ],
                         ),
                    dict(label="Click to Show Linear Trendlines",
                         method="update",
                         args=[
                             {"visible": [True, True, True, False, False, True, False, False]},
                             {"annotations": linear_annotation+test_annotations}
                         ],
                         ),
                    dict(label="Click to Show Exponential Trendlines",
                         method="update",
                         args=[
                             {"visible": [True, True, False, True, False, False, True, False]},
                             {"annotations": exponential_annotations+test_annotations}
                         ],
                         ),
                    dict(label="Click to Show Logarithmic Trendlines",
                         method="update",
                         args=[
                             {"visible": [True, True, False, False, True, False, False, True]},
                             {"annotations": logarithmic_annotations+test_annotations}
                         ],
                         )
                ]
            )],
        annotations=[
            dict(
                text="<b>Add or Remove Trendlines</b>",
                x=1.01, xref="paper",
                xanchor="left",
                y=0.95,
                yref="paper",
                showarrow=False)]
    )

    fig.update_xaxes(title_text="Base Total", row=2, col=1)
    fig.update_yaxes(title_text="Base Egg Steps", row=1, col=1)
    fig.update_yaxes(title_text="Capture Rate", row=2, col=1)

    fig.update_layout(title="Comparison of Pokémon Base Total, Base Egg Steps, and Capture Rate")

    save_plot(fig, "LinkedPlotUpdated")
