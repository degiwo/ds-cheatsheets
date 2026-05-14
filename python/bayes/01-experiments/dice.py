import pandas as pd

"""
Suppose I have a box with a 6-sided die, an 8-sided die and a 12-sided die.
I choose one of the dice at random, roll it and report that the outcome is 1.
What is the probability that I chose the 6-sided die?
"""

# search for P(Die | Outcome)
table = pd.DataFrame(index=["6 Die", "8 Die", "12 Die"])
table["prior"] = 1/3, 1/3, 1/3 # P(Die)
table["likelihood"] = 1/6, 1/8, 1/12 # P(Outcome | Die)
table["unnorm"] = table["prior"] * table["likelihood"] # P(Die) * P(Outcome | Die)
prob_data = table["unnorm"].sum()
table["posterior"] = table["unnorm"] / prob_data # P(Die | Outcome)

print(table)
