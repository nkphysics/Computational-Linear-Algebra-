# Computational Linear Algebra Ep#7 Cholesky Decomposition
# By: Nick Space Cowboy

import numpy as np
from lin_alg import lin_alg

if __name__ == "__main__":
	A = np.array([[np.random.randint(1, 100), 2, 6],
				  [2, np.random.randint(1, 100), 5],
				  [6, 5, np.random.randint(1, 100)]])
	print(f"A: {A}")
	L = lin_alg.cholesky(A)
	print(f"L: {L}")
	check = A - np.dot(L, L.T)
	print("Check: ")
	print(check)
