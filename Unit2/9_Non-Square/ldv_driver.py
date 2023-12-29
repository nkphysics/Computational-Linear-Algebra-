# Computational Linear Algebra Ep#9 Non-quare LDV Decomposition
# By: Nick Space Cowboy

import numpy as np
from lin_alg import lin_alg

if __name__ == "__main__":
	A = np.array(np.random.randint (0,100,(4, 6)), dtype=np.float64)
	print("A: ")
	print(A)
	L, D, V = lin_alg.LDV(A)
	print("L:")
	print(L)
	print("D:")
	print(D)
	print("V:")
	print(V)
	print("Check:")
	print((A - np.dot(np.dot(L, D), V)).round())
