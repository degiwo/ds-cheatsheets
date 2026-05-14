import numpy as np
from empiricaldist import Pmf

"""
Bowl n contains n% vanilla cookies, n = 0,...,100
Suppose we choose a bowl at random, choose a cookie at random.
It turns out to be vanilla.
What is the probability that the cookie came from Bowl n?
"""

prior = Pmf.from_seq(list(range(101)))
likelihood_vanilla = [n/100 for n in range(101)]
posterior = prior * likelihood_vanilla
posterior.normalize()

print(posterior[96])

"""
Update posterior after drawing chocolate from the same bowl after returning the vanilla.
"""

likelihood_chocolate = [1-n/100 for n in range(101)]
posterior *= likelihood_chocolate
posterior.normalize()

print(posterior[96])

"""
Which is the bowl with the maximum likelihood of 1 vanilla and 1 chocolate?
"""

print(posterior.max_prob())
