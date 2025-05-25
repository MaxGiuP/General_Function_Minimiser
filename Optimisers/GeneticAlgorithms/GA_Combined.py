import numpy as np
import pandas as pd

def select_mating_pool(values, fitness, random_numbers, method="rank_roulette"):
    """
    Rank-based roulette-wheel selection.
    values: array of individuals
    fitness: array of fitness values (higher = better)
    random_numbers: list of random floats in [0,1]
    """
    if method != "rank_roulette":
        raise ValueError("Unsupported selection method")
    # Sort ascending by fitness (worst→best)
    idx_sorted     = np.argsort(fitness)
    sorted_values  = np.array(values)[idx_sorted]
    # Assign ranks 1..N
    N = len(values)
    ranks = np.arange(1, N+1)
    probs = ranks / ranks.sum()
    cum_probs = np.cumsum(probs)
    # Roulette-wheel
    pool = []
    for r in random_numbers:
        idx = np.where(cum_probs >= r)[0][0]
        pool.append(sorted_values[idx])
    return pool

def reproduce_binary(parents, bounds, bits, random_numbers,
                     crossover_method="single_point", mutation_method="one_bit"):
    """
    Single-point crossover & one-bit mutation for binary-encoded GA.
    parents: list of two real values
    bounds: (lower, upper)
    bits: number of bits
    random_numbers: [r_cross, r_mut1, r_mut2]
    """
    lower, upper = bounds
    # Encoding/decoding
    def encode(val):
        m = round((val - lower) / (upper - lower) * (2**bits - 1))
        return format(m, f'0{bits}b')
    def decode(bin_str):
        m = int(bin_str, 2)
        return lower + m * (upper - lower) / (2**bits - 1)
    p_bits = [encode(p) for p in parents]
    # Crossover
    if crossover_method == "single_point":
        cp = int(random_numbers[0] * (bits - 1)) + 1
        c1 = p_bits[1][:cp] + p_bits[0][cp:]
        c2 = p_bits[0][:cp] + p_bits[1][cp:]
    else:
        raise ValueError("Unsupported crossover method")
    # Mutation
    def mutate(bin_str, r):
        pos = int(r * bits)
        lst = list(bin_str)
        lst[pos] = '1' if lst[pos]=='0' else '0'
        return ''.join(lst)
    c1m = mutate(c1, random_numbers[1])
    c2m = mutate(c2, random_numbers[2])
    # Decode
    return decode(c1m), decode(c2m)

"""
if __name__ == "__main__":
    # Example 1: selection
    values  = [1, 3, 6, 7, 11]
    fitness = [0.1, 0.55, 0.4, 0.2, 0.15]
    rnd_sel = [0.0975, 0.2785, 0.5469, 0.9575, 0.9649]
    pool = select_mating_pool(values, fitness, rnd_sel)
    print("Mating Pool:", pool)
    # Example 2: reproduction
    parents = [-0.42857, 0.04762]
    bounds = (-1, 1)
    bits = 6
    rnd_rep = [0.3772, 0.1397, 0.8425]
    child1, child2 = reproduce_binary(parents, bounds, bits, rnd_rep)
    print("Offspring:", (round(child1,5), round(child2,5)))
"""