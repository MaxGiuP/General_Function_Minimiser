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
    v = np.array(relative_importance, dtype=float)
    # Build pairwise matrix: P[i,j] = v[i] / v[j]
    P = v[:, None] / v[None, :]

    # Eigen-decomposition
    vals, vecs = np.linalg.eig(P)
    # Pick the eigenvector associated with the largest (real) eigenvalue
    idx = np.argmax(vals.real)
    w = vecs[:, idx].real
    w = w / np.sum(w)

    lambda_max = vals[idx].real
    return P, w, lambda_max