"""
A genetic algorithmn using six bit binary encoding, with the highest bit to the left, is being used to improve a design. Two designs selected as parents for cross-over have values of 0.599 and 0.888 where the lower and upper bounds of these design variables are -2 and 1, respectively.

Random numbers in the range (0,1) are used to decide the distance of the cut-point from the left-hand end of the strings. The random number to be used in this case is 0.3035.

What is the design variable value of the child produced from the left-hand end of parent one and the right-hand end of parent two?

Give your answer to three significant figures including any trailing zeros if necessary.
"""


lower, upper, bits = -2, 1, 6
parent1, parent2 = 0.599, 0.888
r_crossover = 0.3035

def encode(val):
    m = round((val - lower) / (upper - lower) * (2**bits - 1))
    return format(int(m), f'0{bits}b')

def decode(bin_str):
    m = int(bin_str, 2)
    return lower + m * (upper - lower) / (2**bits - 1)

b1 = encode(parent1)
b2 = encode(parent2)

cp = int(r_crossover * (bits - 1)) + 1

child_bits = b1[:cp] + b2[cp:]

child_value = decode(child_bits)

print(f"Parent1 bits   = {b1}")
print(f"Parent2 bits   = {b2}")
print(f"Crossover point= {cp}")
print(f"Child bits     = {child_bits}")
print(f"Child value    = {child_value:.6f}")
print(f"Rounded (3sf)  = {child_value:.3f}")
