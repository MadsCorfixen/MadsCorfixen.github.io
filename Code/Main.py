import Plots as plts
import DataManipulation as dm
import plotly.graph_objects as go
import statistics
import Regression as rgr


# plts.create_type_histogram()
# plts.create_scatter_with_stats()
# plts.create_legend_violin_plot(False, False, "ViolinPlot")
# plts.create_legend_violin_plot(True, True, "ViolinPlotWithPoints")
# plts.create_legend_boxplot()
# plts.linked_plot()


all_data = dm.load_data()
data = dm.group_data_mean(data=all_data, group_by_var="base_total")
