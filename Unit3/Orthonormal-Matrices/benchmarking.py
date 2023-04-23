import numpy as np
from time import perf_counter_ns
import matplotlib.pyplot as plt


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
    
    
def makematrices(n):
    A = np.array(np.random.randint(0, 256, (n, n)), dtype=np.float64)
    b = np.array(np.random.randint(0, 256, (n, 1)), dtype=np.float64)
    Q = gram_schmidt(A)
    return A, Q, b

if __name__ == "__main__":
    benchstats = {"n":[],
                  "A Times": [],
                  "Q Times": []
                 }
    for n in np.arange(100, 1025, 25):
        benchstats["n"].append(n)
        A, Q, b = makematrices(n)
        # Begin benchmarking Ax=b
        start_A = perf_counter_ns()
        x1 = np.linalg.solve(A, b)
        end_A = perf_counter_ns()
        atime = (end_A - start_A)/ 1000
        benchstats["A Times"].append(atime)
        # Begin benchmarking Qx = b
        start_Q = perf_counter_ns()
        x2 = np.linalg.solve(Q, b)
        end_Q = perf_counter_ns()
        qtime = (end_Q - start_Q)/ 1000
        benchstats["Q Times"].append(qtime)
    
    plt.style.use("dark_background")
    fig, a = plt.subplots()
    a.plot(benchstats["n"], benchstats["A Times"], label=r"$ A \vec{x} = \vec{b}$")
    a.plot(benchstats["n"], benchstats["Q Times"], label=r"$ Q \vec{x} = \vec{b}$")
    a.set_yscale("log")
    a.set_title("Orthonormal Benchmarking")
    a.set_ylabel(r"Runtime ($ms$)")
    a.set_xlabel(r"$n \times n$ matrix dimensions")
    plt.legend()
    plt.show()
