"""
4. A genetic algorithm is being used to maximize a single valued
function with five members in its population and a total
replacement, rank based, roulette wheel strategy for selecting
the mating pool. The selection probabilities are arranged on the
roulette wheel in ascending order with worst member first. Given
that the population members to be chosen from have variable
values of 1, 3, 6, 7 and 11 and their objective functions are 0.1,
0.55, 0.4, 0.2 and 0.15, respectively, decide the makeup of the
mating pool using the following five random numbers in the
range 0-1: 0.0975, 0.2785, 0.5469, 0.9575 and 0.9649.
"""

import numpy as np
import pandas as pd

values  = np.array([1, 3, 6, 7, 11])
fitness = np.array([0.1, 0.55, 0.4, 0.2, 0.15])
rand_nums = np.array([0.0975, 0.2785, 0.5469, 0.9575, 0.9649])

idx_sorted       = np.argsort(fitness)
sorted_values    = values[idx_sorted]
sorted_fitness   = fitness[idx_sorted]

ranks = np.arange(1, len(values) + 1)

probs      = ranks / ranks.sum()
cum_probs  = np.cumsum(probs)


mating_pool = []
for r in rand_nums:
    pick = np.where(cum_probs >= r)[0][0]
    mating_pool.append(sorted_values[pick])

result = pd.DataFrame({
    'Random Number': rand_nums,
    'Selected Value (THESE VALUES)': mating_pool
})
print(result)
