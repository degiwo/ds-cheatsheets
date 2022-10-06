import pandas as pd

earthquakes = pd.read_csv("earthquakes.csv")

# Group by
earthquakes.groupby("alert")["mag", "gap"].mean()

# Multiple aggregations
earthquakes.groupby("alert")["mag", "gap"].agg(["min", "max", "mean"])
