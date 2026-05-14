import pandas as pd
import seaborn as sns

earthquakes = pd.read_csv("earthquakes.csv")

# Boxplot by group
sns.boxplot(
    data=earthquakes,
    x="status",
    y="mag"
).set_title("Boxplot")

# Pairplot
sns.pairplot(
    data=earthquakes[["mag", "gap", "magType", "nst"]],
    hue="magType"
)
