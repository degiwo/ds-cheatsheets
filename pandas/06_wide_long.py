import pandas as pd

earthquakes = pd.read_csv("earthquakes.csv")

# Transpose
earthquakes.T.iloc[:, :2]

# Melt: wide to long
earthquakes_long = earthquakes[["ids", "mag", "place"]].melt(
    id_vars="ids"
)

# Pivot: long to wide
earthquakes_wide = earthquakes_long.pivot(
    index="ids",
    columns="variable",
    values="value"
)
