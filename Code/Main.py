import Plots as plts
import DataManipulation as dm

data = dm.load_data()

plts.create_type_histogram()
plts.create_scatter_with_stats()
plts.create_legend_violin_plot()
