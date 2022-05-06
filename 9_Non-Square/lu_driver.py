# Computational Linear Algebra Ep#9 Non-Square Lu Decomposition
# By: Nick Space Cowboy

import numpy as np
from lin_alg import lin_alg

if __name__ == "__main__":
	# generate A matrix
	A = np.array(np.random.randint (1,100,(3,7)), dtype=np.float64)
	print("A: ")
	print(A)
	# perform LU decomposition with our LinAlg LU function
	L, U = lin_alg.LU(A)
	print("L: ")
	print(L)
	print("U: ")
	print(U)
	print("Check: ")
	# Check that LU=A
	print((A - np.dot(L,U)).round())
