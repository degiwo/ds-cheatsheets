import pandas as pd

earthquakes = pd.read_csv("earthquakes.csv")

# Select columns
earthquakes.alert
earthquakes[["mag", "title"]]
earthquakes[[col for col in earthquakes.columns if "mag" in col]]

# Slicing
earthquakes[42:45]
earthquakes[["mag", "title"]][42:45]

# Indexing: Look up and replace
earthquakes.at[10, "mag"]
earthquakes.iloc[30:33, 8:11]
earthquakes.loc[2:10, "title"] = earthquakes.loc[2:10, "title"].str.lower()

# Filtering
earthquakes[earthquakes["mag"] >= 7]
earthquakes.loc[earthquakes["mag"] >= 7, ["title", "alert"]]
earthquakes.loc[earthquakes["mag"] >= 7] \
    .loc[earthquakes["alert"].isin(["red", "green"])] \
    .loc[:, ["title", "alert"]]
