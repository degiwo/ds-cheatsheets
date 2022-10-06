import pandas as pd

earthquakes = pd.read_csv("earthquakes.csv")

# Examine
earthquakes.shape
earthquakes.head()
earthquakes.info()

# Describe
earthquakes.describe()
earthquakes.describe(include=object)

# Statistics
earthquakes.count()
earthquakes["alert"].count()
earthquakes["cdi"].sum()
earthquakes["magType"].value_counts()

# Index
earthquakes.index.max()

# Sort
earthquakes.sort_values(by="mag")
