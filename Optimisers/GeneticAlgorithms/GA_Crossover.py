"""4. Produce two new members of a population from two parents
using single point cross-over and one bit random mutation of
both children, for a binary encoded Genetic Algorithm with 6 bits.
The two parents are -0.42857 and 0.04762 and the upper and
lower bounds on the variables are -1 and 1.
The next three random numbers available from your random
number generator, which generates numbers in the interval 0-1,
are assumed to be 0.3772, 0.1397 and 0.8425."""

import numpy as np
import pandas as pd

# GA settings
lower, upper = 0, 1
bits = 6
parents = [0.599, 0.888]
random_nums = [0, 0.3035, 0.6789]  # crossover, mutation1, mutation2

# Encoding and decoding functions
def encode(val):
    m = round((val - lower) / (upper - lower) * (2**bits - 1))
    return format(int(m), f'0{bits}b')

def decode(bin_str):
    m = int(bin_str, 2)
    return lower + m * (upper - lower) / (2**bits - 1)

# 1) Parent bitstrings
p_bits = [encode(p) for p in parents]

# 2) Single-point crossover (swap child roles)
cp = int(random_nums[0] * (bits - 1)) + 1
c1 = p_bits[1][:cp] + p_bits[0][cp:]  # child1: parent2|parent1
c2 = p_bits[0][:cp] + p_bits[1][cp:]  # child2: parent1|parent2

# 3) One‐bit mutation
def mutate(bin_str, r):
    pos = int(r * bits)
    lst = list(bin_str)
    lst[pos] = '1' if lst[pos]=='0' else '0'
    return ''.join(lst), pos

c1m, pos1 = mutate(c1, random_nums[1])
c2m, pos2 = mutate(c2, random_nums[2])

# 4) Decode children
child_vals = [round(decode(c1m), 5), round(decode(c2m), 5)]

# 5) Display steps
df = pd.DataFrame({
    'Step': [
        'Parent A', 'Parent B',
        'Crossover Point',
        'Child1 Pre-Mutation', 'Child2 Pre-Mutation',
        'Mutation Pos Child1', 'Mutation Pos Child2',
        'Child1', 'Child2'
    ],
    'Result': [
        parents[0], parents[1],
        cp,
        c1, c2,
        pos1, pos2,
        child_vals[0], child_vals[1]
    ]
})
print(df)
