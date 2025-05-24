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


def roulette(values, fitness, rand_nums):
    values   = np.asarray(values)
    fitness  = np.asarray(fitness)
    rand_nums = np.asarray(rand_nums)

    # 1) Rank individuals by fitness, ascending (worst first)
    idx_sorted     = np.argsort(fitness)
    sorted_values  = values[idx_sorted]
    # 2) Assign ranks 1..N to sorted list, compute selection probs
    N = len(values)
    ranks = np.arange(1, N+1)
    probs = ranks / ranks.sum()
    cum_probs = np.cumsum(probs)

    # 3) For each random number, find the first cum_prob ≥ r
    picks = np.searchsorted(cum_probs, rand_nums, side='right')
    mating_pool = sorted_values[picks]

    # 4) Build a DataFrame for clarity
    df = pd.DataFrame({
        'Random Number': rand_nums,
        'Selected Value': mating_pool
    })

    return mating_pool, df