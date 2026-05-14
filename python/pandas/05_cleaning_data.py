import pandas as pd

earthquakes = pd.read_csv("earthquakes.csv")

# Rename columns
earthquakes.rename(columns={
    "cdi": "CDI"
})
earthquakes.rename(str.upper, axis=1)

# Cast datetime
earthquakes["date"] = "2021-01-01"
earthquakes["date"] = pd.to_datetime(earthquakes["date"])

# Cast categories
earthquakes["alert"] = earthquakes["alert"].astype("category")
