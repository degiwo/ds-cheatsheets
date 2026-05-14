import pandas as pd

earthquakes = pd.read_csv("earthquakes.csv")

# Scatterplot
earthquakes[:100].plot(
    kind="scatter",
    x="gap",
    y="mag"
)

# Distribution
earthquakes.plot(
    kind="kde",
    y="mag",
    title="Distribution of mag"
)

# Boxplot
earthquakes[["mag", "gap", "nst"]].plot(
    kind="box"
)

# Counts
earthquakes["status"].value_counts().plot(
    kind="bar"
)
