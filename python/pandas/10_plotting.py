import pandas as pd
import matplotlib.pyplot as plt

earthquakes = pd.read_csv("earthquakes.csv")

# Basic plot
plt.plot(earthquakes.loc[:100, "mag"])
plt.show()

# Histogram
earthquakes \
    .loc[earthquakes["alert"] == "green"]["mag"] \
    .pipe(plt.hist)
plt.show()
