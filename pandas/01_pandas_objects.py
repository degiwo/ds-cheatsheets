import pandas as pd

language_dataframe = pd.DataFrame({
    "language": ["Python", "R", "Julia", "Java", "JavaScript", "C", "C++"],
    "level": [3, 4, 1, 1, 0, 2, 2]
})
language_series = pd.Series(language_dataframe["language"])

# DataFrame attributes
language_dataframe.index
language_dataframe.values
language_dataframe.columns
language_dataframe.dtypes

# Series attributes
language_series.index
language_series.values
language_dataframe.dtypes
