import pandas as pd

earthquakes = pd.read_csv("earthquakes.csv")

# Create new column
earthquakes["source"] = "UGSG API"
earthquakes["place_num"] = earthquakes["place"].str.extract(r"^(\d*)")

# Create multiple columns
earthquakes[4:8][["place", "alert"]].assign(
    in_ca=earthquakes["place"].str.endswith("CA"),
    in_alaska=earthquakes["place"].str.endswith("Alaska"),
    neither=lambda x: ~x["in_ca"] & ~x["in_alaska"]
)

# Bind DataFrames
pd.concat([earthquakes[:2], earthquakes[2:4]])
pd.concat([earthquakes["mag"][:4], earthquakes["place"][:4]], axis=1)

# Pop column
place_num = earthquakes.pop("place_num")
earthquakes[place_num == "9"]
