# Computational Linear Algebra Ep#5 Lu Decomposition with numpy
# By: Nick Space Cowboy

import numpy as np
from scipy import linalg

if __name__ == "__main__":
	A = np.array(np.random.randint (0,100,(4,4)), dtype=np.float64)
	print("A: ")
	print(A)
	P, L, U = linalg.lu(A, permute_l=False)
	print("L: ")
	print(L)
	print("U: ")
	print(U)
	print("Check")
	# Check that LU=A
	PL = np.dot(P,L)
	print(np.dot(PL,U))
