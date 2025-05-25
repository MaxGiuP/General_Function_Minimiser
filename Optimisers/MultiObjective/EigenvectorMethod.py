"""
3. The eigenvector method is to be used to assign objective
function weights to a problem with three goals. Goal 1 is
considered to be twice as important as goal 2, which in turn is
three times as important as goal 3. By assuming the appropriate
largest eigenvalue for consistent input data, derive the resulting
normalized weight vector.
"""
import numpy as np

def eigenvector_weights(relative_importance):
    # 1) build numeric array
    v = np.array(relative_importance, dtype=float)

    # 2) build pairwise matrix
    P = v[:, None] / v[None, :]

    # 3) eigen-decomposition
    vals, vecs = np.linalg.eig(P)
    idx = np.argmax(vals.real)
    w = vecs[:, idx].real
    w = w / np.sum(w)
    lambda_max = vals[idx].real

    # 4) format output
    lines = []
    lines.append("Pairwise comparison matrix P:\n")
    for row in P:
        lines.append("  [" + ", ".join(f"{val:.4f}" for val in row) + "]\n")
    lines.append("\nNormalized weight vector w:\n")
    lines.append("  [" + ", ".join(f"{wi:.4f}" for wi in w) + "]\n")
    lines.append(f"\nPrincipal eigenvalue λ_max = {lambda_max:.4f}\n")

    return "".join(lines)


"""
# Example usage:
if __name__ == "__main__":
    rel_imp = [1, 1/1.97, 1/(1.43*1.97)]
    result = eigenvector_weights_str(rel_imp)
    print(result)
"""