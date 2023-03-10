# Computational Linear Algebra Ep#15 Gram-Schmidt Process
# By: Nick Space Cowboy

import numpy as np

def gram_schmidt(A):
    m, n  = A.shape
    Q = np.zeros((m, n))
    Q[:, 0] = A[:, 0] / np.linalg.norm(A[:, 0], 2)
    for i in range(1, n):
        Q[:, i] = A[:, i]
        for j in range(0, i):
            inner = np.dot(Q[:, j].T, Q[:, i])
            Q[:, i] = Q[:, i] - np.dot(inner, Q[:, j])
        Q[:, i] = Q[:, i] / np.linalg.norm(Q[:, i], 2)
    return Q


if __name__ == "__main__":
    A = np.array(np.random.randint (0, 10, (3, 3)), dtype=np.float64)
    print("A: ")
    print(A)
    print("Q: ")
    Q = gram_schmidt(A)
    print(Q)
    I = np.dot(Q.T, Q)
    print("Check: ")
    print(I)
    print(np.round(I))
    
