"""
You take an experiment in your classroom:
- You ask how many people were born on May 11: 2 people raise their hand
- You ask how many people were born on May 23: 1 person raise their hand
- You ask how many were born on Aug 1: no one raises their hand
How many people are in the classroom?
What is the probablility that there are more than 1200?
"""

import numpy as np
from empiricaldist import Pmf
from scipy.stats import binom

hypos = np.arange(1, 10000) # possible numbers of people
prior = Pmf(1, hypos)

def update(pmf, data):
    # for any given N, what is the likelihood of seeing the data
    hypos = pmf.qs
    likelihood = binom.pmf(data, hypos, 1/365)
    impossible = (data > hypos)
    likelihood[impossible] = 0
    pmf *= likelihood
    pmf.normalize()

posterior = prior.copy()
for data in [2, 1, 0]:
    update(posterior, data)

print(posterior.max_prob())
print(posterior[1200:].sum())
