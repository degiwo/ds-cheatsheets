import pandas as pd

"""
Suppose you meet someone and learn that they have two children.
You ask if either child is a girl and they say yes.
What is the probability that both children are girls?
"""

# search for P(Girl | Answer)
table = pd.DataFrame(index=["Girl", "Boy"])
table["prior"] = 1/2, 1/2
table["likelihood"] = 1, 1/2
table["unnorm"] = table["prior"] * table["likelihood"]
prob_data = table["unnorm"].sum()
table["posterior"] = table["unnorm"] / prob_data

print(table)
