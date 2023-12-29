# Computational Linear Algebra Ep#8 LDL^T Decomposition
# By: Nick Space Cowboy

import numpy as np
from lin_alg import lin_alg

if __name__ == "__main__":
	A = np.array([[np.random.randint(1, 100), 2, 6],
				  [2, np.random.randint(1, 100), 5],
				  [6, 5, np.random.randint(1, 100)]])
	print("A: ")
	print(A)
	L, D = lin_alg.LDLT(A)
	print("L:")
	print(L)
	print("D:")
	print(D)
	print("Check:")
	print((A - np.dot(np.dot(L, D), L.T)).round())
