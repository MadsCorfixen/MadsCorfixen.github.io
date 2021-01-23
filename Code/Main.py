import Plots as plts

# Creates the histogram to find the most common Pokémon typing.
plts.create_type_histogram()

# Creates the coloured scatter plot to see correlation between Base Total, Base Egg Steps, and Capture Rate.
plts.create_scatter_with_stats()

# Creates the linked plot to see correlation between Base Total, Base Egg Steps, and Capture Rate.
plts.linked_plot()

# Creates the unethical violin plot (no points, no sample size) to see what makes a Pokémon legendary.
plts.create_legend_violin_plot(False, False, "ViolinPlot")

# Creates the violin plot (including jittered points and sample size) to see what makes a Pokémon legendary.
plts.create_legend_violin_plot(True, True, "ViolinPlotWithPoints")

# Creates the boxplot to see what makes a Pokémon legendary.
plts.create_legend_boxplot()
