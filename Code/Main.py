import Plots as Plt
import DataManipulation as Dm
import pandas as pd
import numpy as np


def main():
    data = Dm.load_data()
    grouped_data = Dm.group_data_mean("base_total")

    print(grouped_data["capture_rate"])
    print(data["capture_rate"])

    Plt.create_scatter_with_stats(grouped_data, x_var="capture_rate", y_var="base_egg_steps", colour_by="base_total",
                                  plot_number=1)


main()
