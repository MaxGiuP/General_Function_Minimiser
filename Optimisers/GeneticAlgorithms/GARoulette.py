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

def roulette(
    individuals,
    fitness,
    rands,
    method: str       = "rank",       # "fitness" or "rank"
    order: str        = "ascending",  # "ascending"=worst-first, "descending"=best-first
    rank_power: float = 1.0,          # exponent p when method="rank"
    replacement: bool = True          # True=with-replacement, False=without
):
    """
    Roulette‐wheel selection that returns a single formatted string,
    including a table of random numbers and selected values.
    """
    vals = np.array(individuals)
    f    = np.array(fitness,   dtype=float)
    r    = np.array(rands,     dtype=float)
    N    = len(vals)

    # 1) Build sorted_vals and weights for rank-based
    if method == "fitness":
        sorted_vals = vals.copy()
        weights     = f.copy()
    else:
        idx_sorted  = np.argsort(f)            # ascending fitness ⇒ worst first
        sorted_vals = vals[idx_sorted]
        ranks       = np.arange(1, N+1, dtype=float)
        weights     = ranks**rank_power

    # 2) Apply order flip for best-first
    if order == "descending":
        sorted_vals = sorted_vals[::-1]
        weights     = weights[::-1]
    elif order != "ascending":
        raise ValueError("order must be 'ascending' or 'descending'")

    # 3) Normalize & cumulative sum
    probs = weights / weights.sum()
    cum   = np.cumsum(probs)

    # 4) Draw
    pool  = []
    sval  = sorted_vals.copy()
    wght  = weights.copy()
    cum_l = cum.copy()
    for rr in r:
        i = np.searchsorted(cum_l, rr, side="right")
        pool.append(int(sval[i]))
        if not replacement:
            sval = np.delete(sval, i)
            wght = np.delete(wght, i)
            if len(wght)==0:
                break
            p_loc = wght / wght.sum()
            cum_l = np.cumsum(p_loc)

    # 5) Build output string
    lines = []
    lines.append("Mating pool: " + ", ".join(str(x) for x in pool) + "\n\n")
    lines.append("Random Number | Selected\n")
    lines.append("--------------|---------\n")
    for rn, sel in zip(r[:len(pool)], pool):
        lines.append(f"   {rn:>10.4f} | {sel}\n")
    return "".join(lines)


# ── Test ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    parents = [1, 3, 6, 7, 11]
    fitness = [0.1, 0.55, 0.4, 0.2, 0.15]
    rands   = [0.0975, 0.2785, 0.5469, 0.9575, 0.9649]

    result = roulette_selection_str(
        individuals=parents,
        fitness=fitness,
        rands=rands,
        method="rank",
        order="ascending",
        rank_power=1.0,
        replacement=True
    )
    print(result)
