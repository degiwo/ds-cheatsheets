"""Time series modeling for stocks."""

import pandas as pd
from sklearn.linear_model import LinearRegression


class StockModeler():
    """Abstract class for methods to model stock."""
    def __init__(self) -> None:
        """
        Nothing happens.
        """
        pass

    def regression(self, data: pd.DataFrame):
        """
        Create linear regression of stock data.

        Parameters:
            - data: pandas.DataFrame with stock data

        Returns:
            - scikit-learn model fitted with stock data of lag=1
        """
        X = data[["Close", "Open"]].shift().dropna()
        y = data["Close"][1:]
        model = LinearRegression().fit(X, y)
        return model
