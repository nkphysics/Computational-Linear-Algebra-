# Computational Linear Algebra Ep#10 Least-Squares w/ built in numpy.linalg.lsq
# By: Nick Space Cowboy

import numpy as np
from time import perf_counter

if __name__ == "__main__":
	# generate A matrix
	A = np.array(np.random.randint(1,100,(3,2)), dtype=np.float64)
	print("A: ")
	print(A)
	b = np.array(np.random.randint(-100, 100, (3, 1)), dtype=np.float64)
	print("b:")
	print(b)
	start = perf_counter()
	lsq = np.linalg.lstsq(A, b, rcond=None)
	x = lsq[0]
	norm = lsq[1][0]**(0.5)
	end = perf_counter()
	print("x:")
	print(x)
	print(f"Norm: {norm}")
	print("Check:")
	print(b - np.dot(A, x))
	print(f"Runtime: {end - start} s")
	
