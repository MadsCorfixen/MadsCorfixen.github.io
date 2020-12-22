import Plots as plts
import DataManipulation as dm

data = dm.load_data()
print(data.columns)

plts.create_type_histogram()
plts.create_scatter_with_stats()

