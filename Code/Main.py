import Plots as plts
import DataManipulation as dm
import plotly.graph_objects as go
import statistics


plts.create_type_histogram()
plts.create_scatter_with_stats()
plts.create_legend_violin_plot(False, False, "ViolinPlot")
plts.create_legend_violin_plot(True, True, "ViolinPlotWithPoints")
plts.create_legend_boxplot()
plts.linked_plot()
