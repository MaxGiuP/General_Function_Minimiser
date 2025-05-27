import numpy as np
import sympy as sp

# ── Selection Operator ──────────────────────────────────────────────────────
def roulette_selection_indices(
    fitness,
    num_select,
    method: str = "rank",
    order: str = "ascending",
    rank_power: float = 1.0,
    replacement: bool = True,
    rands: list = None,
    rng: np.random.Generator = None
):

    f = np.array(fitness, dtype=float)
    N = len(f)
    if rands is None:
        rng = rng or np.random.default_rng()
        rands = rng.random(num_select).tolist()
    if len(rands) < num_select:
        raise ValueError("Not enough random numbers provided")

    if method == "fitness":
        avail_idx     = list(range(N))
        avail_weights = f.tolist()
    else:
        sorted_order  = np.argsort(f)
        avail_idx     = sorted_order.tolist()
        avail_weights = (np.arange(1, N+1, dtype=float)**rank_power).tolist()

    if order == "Descending":
        avail_idx.reverse()
        avail_weights.reverse()
    elif order != "Ascending":
        raise ValueError("order must be 'Ascending' or 'Descending'")

    selected = []
    for rr in rands[:num_select]:
        w = np.array(avail_weights, dtype=float)
        p = w / w.sum()
        cum = np.cumsum(p)
        pick = np.searchsorted(cum, rr, side="right")
        idx  = avail_idx[pick]
        selected.append(idx)
        if not replacement:
            avail_idx.pop(pick)
            avail_weights.pop(pick)
            if not avail_idx:
                break

    return selected


# ── Reproduction Operator ────────────────────────────────────────────────────
def reproduce_parametric(
    parents,
    lower, upper,
    bits,
    crossover_point: int = None,
    mutation_positions: list = None,
    rng: np.random.Generator = None
):
    """
    Single‐point crossover + one‐bit mutation.
    Returns two decoded real children.
    If `crossover_point` or `mutation_positions` are None, draws from `rng`.
    """
    rng = rng or np.random.default_rng()

    def encode(x):
        m = round((x - lower) / (upper - lower) * (2**bits - 1))
        return format(int(m), f"0{bits}b")
    def decode(bs):
        m = int(bs, 2)
        return lower + m * (upper - lower) / (2**bits - 1)
    def mutate(bs, pos):
        lst = list(bs)
        lst[pos] = "1" if lst[pos]=="0" else "0"
        return "".join(lst)
        
    pA, pB = parents
    bA, bB  = encode(pA), encode(pB)

    if crossover_point is None:
        cp = int(rng.random() * (bits - 1)) + 1
    else:
        cp = crossover_point
    if not (1 <= cp < bits):
        raise ValueError(f"crossover_point must be in [1..{bits-1}]")

    c1_pre = bB[:cp] + bA[cp:]
    c2_pre = bA[:cp] + bB[cp:]

    if mutation_positions == []:
        c1_mut = c1_pre
        c2_mut = c2_pre
    else:

        if mutation_positions is None:
            pos1 = int(rng.random() * bits)
            pos2 = int(rng.random() * bits)
        else:
            pos1, pos2 = mutation_positions
        if not (0 <= pos1 < bits and 0 <= pos2 < bits):
            raise ValueError(f"mutation_positions must be in [0..{bits-1}]")
        c1_mut = mutate(c1_pre, pos1)
        c2_mut = mutate(c2_pre, pos2)

    child1 = decode(c1_mut)
    child2 = decode(c2_mut)

    return child1, child2


# ── Full GA Engine ─────────────────────────────────────────────────────────
class GeneticAlgorithm:
    def __init__(
        self,
        fitness_fn, 
        lower, upper, bits,
        pop_size,
        generations,
        select_params: dict = None,
        crossover_rate: float = 0.9,
        mutation_rate: float  = 1.0, 
        rng: np.random.Generator = None
    ):
        x = sp.symbols("x", real=True)
        expr = sp.sympify(fitness_fn)
        f_num = sp.lambdify(x, expr, 'numpy')
        fitness_formula = lambda v: float(f_num(v))

        self.fitness_fn    = fitness_formula
        self.lower, self.upper = lower, upper
        self.bits          = bits
        self.pop_size      = pop_size
        self.generations   = generations
        self.select_params = select_params or {}
        self.cx_rate       = crossover_rate
        self.mut_rate      = mutation_rate
        self.rng           = rng or np.random.default_rng()

        self.population = self.rng.uniform(lower, upper, size=pop_size)

    def evaluate(self):
        return np.array([self.fitness_fn(x) for x in self.population], dtype=float)

    def select(self):
        fit   = self.evaluate()
        idxs  = roulette_selection_indices(
            fitness    = fit.tolist(),
            num_select = self.pop_size,
            rng        = self.rng,
            **self.select_params
        )
        return idxs

    def reproduce(self, parent_idxs):
        next_pop = []
        for i in range(0, self.pop_size, 2):
            i1, i2 = parent_idxs[i], parent_idxs[i+1]
            p1, p2 = self.population[i1], self.population[i2]
            cp = None
            if self.rng.random() < self.cx_rate:
                cp = int(self.rng.random() * (self.bits - 1)) + 1

            mut_pos = None
            if self.rng.random() < self.mut_rate:
                mut_pos = [
                    int(self.rng.random() * self.bits),
                    int(self.rng.random() * self.bits)
                ]
            c1, c2 = reproduce_parametric(
                parents            = [p1, p2],
                lower              = self.lower,
                upper              = self.upper,
                bits               = self.bits,
                crossover_point    = cp,
                mutation_positions = mut_pos,
                rng                = self.rng
            )
            next_pop.extend([c1, c2])
        self.population = np.array(next_pop[:self.pop_size])

    def run(self):
        best_x, best_f = None, -np.inf
        for _ in range(self.generations):
            fit = self.evaluate()

            i_max = np.argmax(fit)
            if fit[i_max] > best_f:
                best_f = fit[i_max]
                best_x = self.population[i_max]

            parents = self.select()
            self.reproduce(parents)
        return best_x, best_f


"""
# ── Example Usage ────────────────────────────────────────────────────────
if __name__ == "__main__":

    # — Exam Q2: roulette only —
    values  = [1,3,6,7,11]
    fitness = [0.1,0.55,0.4,0.2,0.15]
    rands   = [0.0975,0.2785,0.5469,0.9575,0.9649]
    idxs = roulette_selection_indices(
        fitness    = fitness,
        num_select = len(values),
        method     = "rank",
        order      = "ascending",
        rank_power = 1.0,
        replacement= True,
        rands      = rands
    )
    pool = [values[i] for i in idxs]
    print("Roulette Pool:", pool)  # [11,7,6,3,3]

    # — Exam Q4: reproduce only —
    parents     = [-0.42857, 0.04762]
    cp          = int(0.3772 * (6-1))
    mut_pos     = [int(0.1397*6), int(0.8425*6)]  # [0,5]
    c1, c2 = reproduce_parametric(
        parents            = parents,
        lower              = -1.0,
        upper              = 1.0,
        bits               = 6,
        crossover_point    = cp,
        mutation_positions = mut_pos
    )
    print("Children:", (round(c1,5), round(c2,5)))
    # → (-0.93651, -0.49206)

    # — Practical GA run —
    def make_fitness_fn(f_str, var_name='x'):
        x = sp.symbols(var_name, real=True)
        expr = sp.sympify(f_str)
        f_num = sp.lambdify(x, expr, 'numpy')
        return lambda v: float(f_num(v))
    
    fitness_fn = make_fitness_fn("-(x-0.3)**2 + 1")

    ga = GeneticAlgorithm(
        fitness_fn    = fitness_fn,
        lower         = -1.0,
        upper         =  1.0,
        bits          =  6,
        pop_size      = 10,
        generations   = 20,
        select_params = {"method":"rank","order":"ascending","rank_power":1.0},
        crossover_rate= 0.8,
        mutation_rate = 0.2,
        rng           = None #np.random.default_rng()
    )
    best_x, best_f = ga.run()
    print("GA best:", best_x, "fitness:", best_f)
"""