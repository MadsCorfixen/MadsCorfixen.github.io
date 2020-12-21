import Plots as Plt
import DataManipulation as Dm


def main():
    data = Dm.load_data()
    Plt.create_type_histogram(data)


main()
