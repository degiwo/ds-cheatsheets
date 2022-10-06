import pandas as pd

earthquakes = pd.read_csv("earthquakes.csv")

# Apply functions
earthquakes[["gap", "mag"]].apply(
    lambda x: x ** 2
)

# Piping
earthquakes\
    .pipe(lambda x: x.loc[:3, ["mag", "gap"]])

# Binning
earthquakes["mag_bin"] = pd.cut(
    earthquakes["mag"], bins=3, labels=["low", "med", "high"]
)
