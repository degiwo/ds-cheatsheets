"""Gather stock data."""

from datetime import datetime
from typing import Optional
import re

import pandas as pd
from pandas_datareader import get_data_yahoo


class StockReader():
    """A class for reading data from the internet."""
    def __init__(self, start: str, end: Optional[str] = None) -> None:
        """
        A StockReader object with date range.

        Parameters:
            - start: string of format "YYYYMMDD", like "20200321"
            - end: string of format "YYYYMMDD", optional. Defaults to today.
        """
        if end is None:
            end = datetime.strftime(datetime.today(), "%Y%m%d")
        self.start, self.end = map(
            lambda x: datetime.strptime(
                re.sub(pattern=r"\D", repl="", string=x), "%Y%m%d"
            ),
            [start, end]
        )

    def get_ticker_data(self, ticker: str) -> pd.DataFrame:
        """
        Get historical data for ticker from Yahoo.

        Parameters:
            - ticker: string of the stock symbol, like "GOOG"

        Returns:
            - pandas.DataFrame with stock data
        """
        return get_data_yahoo(ticker, self.start, self.end)
