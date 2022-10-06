"""Helper functions for classes."""

import pandas as pd


def concatenate_stock_data(mapping: dict) -> pd.DataFrame:
    """
    Create new DataFrame with many stocks and
    a new column indicating the stock.

    Parameters:
        - mapping: dictionary of the form {stock_name: stock_data},
            like {"name1": df1, "name2": df2}

    Returns:
        - pandas.DataFrame with data of all stocks given
    """
    concatenated_df = pd.DataFrame()

    for stock, stock_data in mapping.items():
        df = stock_data.copy()
        df["name"] = stock
        concatenated_df = pd.concat([concatenated_df, df], axis=0)

    return concatenated_df
