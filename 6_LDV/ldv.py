# Computational Linear Algebra Ep#6 LDV Decomposition
# By: Nick Space Cowboy

import numpy as np
from lin_alg import lin_alg

if __name__ == "__main__":
	A = np.array(np.random.randint (0,100,(4,4)), dtype=np.float64)
	print("A: ")
	print(A)
	# perform LU decomposition with our LinAlg LU function
	L, D, V = lin_alg.LDV(A)
	print("L:")
	print(L)
	print("D:")
	print(D)
	print("V:")
	print(V)
	print("Check:")
	print(np.dot(np.dot(L, D), V))
	
