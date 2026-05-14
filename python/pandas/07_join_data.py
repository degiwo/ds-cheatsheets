import pandas as pd

earthquakes = pd.read_csv("earthquakes.csv")
types_mapping = pd.DataFrame({
    "type": ["earthquake", "quarry blast", "explosion", "ice quake", "other event"],
    "type_short": ["EQ", "QB", "EX", "IQ", "Other"]
})

# Inner join
earthquakes.merge(
    types_mapping, on="type"
)

# Left join
earthquakes.merge(
    types_mapping, on="type", how="left"
)
