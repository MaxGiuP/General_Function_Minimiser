"""
3. The eigenvector method is to be used to assign objective
function weights to a problem with three goals. Goal 1 is
considered to be twice as important as goal 2, which in turn is
three times as important as goal 3. By assuming the appropriate
largest eigenvalue for consistent input data, derive the resulting
normalized weight vector.
"""

import numpy as np

def eigenvector_weights(P):
    """
    Given a pairwise preference matrix P (n×n), compute the principal
    eigenvector w and its eigenvalue λmax, then normalize w so that sum(w)=1.
    Returns:
      w:   normalized weight vector (length n)
      λ:   principal eigenvalue
    """
    vals, vecs = np.linalg.eig(P)
    idx = np.argmax(vals.real)
    w = vecs[:,idx].real
    w /= np.sum(w)
    return w, vals[idx].real

def compute_ahp_weights(relative_importance):
    """
    Given a list `relative_importance` of length n, where
      relative_importance[i] = (absolute) importance of goal i
    (up to a common scale), this builds the pairwise matrix P_ij = v[i]/v[j],
    runs the eigenvector method, and returns (P, w, λ_max).
    """
    v = np.array(relative_importance, dtype=float)
    P = v[:,None] / v[None,:]
    w, λ = eigenvector_weights(P)
    return P, w, λ


P, w, λ = compute_ahp_weights([1, 1/1.97, 1/(1.43*1.97)])
print("Pairwise matrix P =\n", P, "\n")
print("Normalized weights w =", np.round(w,8))
print("Principal eigenvalue λ_max =", round(λ,8))
