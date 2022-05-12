"""
Ask each person to flip a coin without revealing the outcome:
- If they get heads, they report YES.
- If they get tails, honestly answer the question "Do you cheat on your taxes?"
Suppose you survey 100 people this way and get 80 YES and 20 NO.
What is the posterior distribution for the fraction of people who cheat on their taxes?
What is the most likely quantity in the posterior distribution?
"""

import numpy as np
from empiricaldist import Pmf

# search for: distriution of cheat probability
hypos = np.linspace(0, 1, 101) # all possible probabilities
prior = Pmf(1, hypos) # initialize all possible probabilities equally
likelihood_yes = 0.5 + 0.5 * hypos
likelihood_no = 1 - likelihood_yes
likelihood = {
    'y': likelihood_yes,
    'n': likelihood_no
}
dataset = 80 * 'y' + 20 * 'n'
for data in dataset:
    prior *= likelihood[data]
prior.normalize()
posterior = prior.copy()

print(posterior)

# maximum likelihood
print(posterior.max_prob())
