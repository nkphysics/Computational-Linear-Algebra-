# Computational Linear Algebra Ep#5 Lu Decomposition
# By: Nick Space Cowboy

import numpy as np
from lin_alg import lin_alg

if __name__ == "__main__":
	A = np.array(np.random.randint (0,100,(4,4)), dtype=np.float64)
	print("A: ")
	print(A)
	L, U = lin_alg.LU(A)
	print("L: ")
	print(L)
	print("U: ")
	print(U)
	print("Check: ")
	print(np.dot(L,U))
