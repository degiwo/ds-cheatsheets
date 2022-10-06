"""Plot stock data."""

import pandas as pd


class Visualizer():
    """Visualizer class which holds the data to be plotted."""
    def __init__(self, data: pd.DataFrame) -> None:
        """
        Pass stock data as pandas.DataFrame and store it.

        Parameters:
            - data: pandas.DataFrame with stock data
        """
        self.data = data

    def plot_evolution_over_time(self, column: str, **kwargs):
        """
        Plot a column as line chart.

        Parameters:
            - column: name of the column as a string
            - **kwargs: additional paramters for pandas.plot

        Returns:
            - a matplotlib.axes line chart with column as y-axis
        """
        return self.data.plot(y=column, **kwargs)
