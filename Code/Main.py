import Plots as plt
import DataManipulation as dm

# Loads data
data = dm.load_data()
grouped_data = dm.group_data_mean("base_total")

# Create Histogram
"""
plt.create_type_histogram(data)
"""

# Create Scatterplot of Capture Rate / Base Egg Steps / Base Total
"""
plt.create_scatter_with_stats(grouped_data, "capture_rate", "base_egg_steps", "base_total", 1)
"""

