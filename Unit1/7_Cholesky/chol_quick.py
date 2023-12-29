# Computational Linear Algebra Ep#7 Cholesky Decomposition
# By: Nick Space Cowboy

import numpy as np

if __name__ == "__main__":
	A = np.array([[np.random.randint(1, 100), 2, 6],
				  [2, np.random.randint(1, 100), 5],
				  [6, 5, np.random.randint(1, 100)]])
	print("A: ")
	print(A)
	L = np.linalg.cholesky(A)
	print("L: ")
	print(L)
	print("Check: ")
	print(A - np.dot(L, L.T))
