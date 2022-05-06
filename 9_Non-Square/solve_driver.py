# Computational Linear Algebra Ep#9 Non-Square Solving
# By: Nick Space Cowboy

import numpy as np
from lin_alg import lin_alg

if __name__ == "__main__":
	# generate A matrix
	A = np.array(np.random.randint(1,100,(8,5)), dtype=np.float64)
	print("A: ")
	print(A)
	b = np.array(np.random.randint(-100, 100, (8, 1)), dtype=np.float64)
	print("b:")
	print(b)
	U, c = lin_alg.SGE(A, b)
	print("U:")
	print(U)
	print("c:")
	print(c)
	x = lin_alg.back_sub(U, c)
	print("x: ")
	print(x)
	print("Check:")
	print((np.dot(A, x)).round() - b)
