"""4. Produce two new members of a population from two parents
using single point cross-over and one bit random mutation of
both children, for a binary encoded Genetic Algorithm with 6 bits.
The two parents are -0.42857 and 0.04762 and the upper and
lower bounds on the variables are -1 and 1.
The next three random numbers available from your random
number generator, which generates numbers in the interval 0-1,
are assumed to be 0.3772, 0.1397 and 0.8425."""

import numpy as np

def reproduce(
    parents,
    crossover_point: int,
    mutation_rands: tuple,
    lower: float = -1.0,
    upper: float = 1.0,
    bits: int = 6
):
    def encode(val):
        m = round((val - lower) / (upper - lower) * (2**bits - 1))
        return format(int(m), f"0{bits}b")
    def decode(bin_str):
        m = int(bin_str, 2)
        return lower + m * (upper - lower) / (2**bits - 1)
    def mutate(bin_str, r):
        pos = int(r * bits)
        lst = list(bin_str)
        lst[pos] = "1" if lst[pos]=="0" else "0"
        return "".join(lst), pos

    pA, pB = parents
    bA, bB = encode(pA), encode(pB)

    cp = crossover_point
    if not (1 <= cp < bits):
        raise ValueError(f"crossover_point must be in [1..{bits-1}]")
    c1_pre = bB[:cp] + bA[cp:]
    c2_pre = bA[:cp] + bB[cp:]

    r2, r3 = mutation_rands
    c1_mut, pos1 = mutate(c1_pre, r2)
    c2_mut, pos2 = mutate(c2_pre, r3)

    child1 = round(decode(c1_mut), 5)
    child2 = round(decode(c2_mut), 5)

    lines = []
    lines.append(f"{'Step':<24}| Result\n")
    lines.append(f"{'-'*24}|{'-'*12}\n")
    lines.append(f"{'Parent A':<24}| {pA}\n")
    lines.append(f"{'Parent B':<24}| {pB}\n")
    lines.append(f"{'Crossover Point':<24}| {cp}\n")
    lines.append(f"{'Bitstring A':<24}| {bA}\n")
    lines.append(f"{'Bitstring B':<24}| {bB}\n")
    lines.append(f"{'Child1 Pre-Mutation':<24}| {c1_pre}\n")
    lines.append(f"{'Child2 Pre-Mutation':<24}| {c2_pre}\n")
    lines.append(f"{'Mutation Pos Child1':<24}| {pos1}\n")
    lines.append(f"{'Mutation Pos Child2':<24}| {pos2}\n")
    lines.append(f"{'Child1 Post-Mutation':<24}| {c1_mut}\n")
    lines.append(f"{'Child2 Post-Mutation':<24}| {c2_mut}\n")
    lines.append(f"{'Child1 Decoded':<24}| {child1}\n")
    lines.append(f"{'Child2 Decoded':<24}| {child2}\n")
    lines.append(f"\nFinal children: ({child1}, {child2})\n")
    return "".join(lines)


if __name__ == "__main__":
    parents      = [-0.42857, 0.04762]
    r1, r2, r3   = 0.3772, 0.1397, 0.8425

    bits         = 6
    crossover_pt = int(r1 * (bits - 1)) + 1  # = 2

    output = reproduce(
        parents           = parents,
        crossover_point   = crossover_pt,
        mutation_rands    = (r2, r3),
        lower             = -1.0,
        upper             =  1.0,
        bits              = bits
    )

    print(output)
