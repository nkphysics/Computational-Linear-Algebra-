# Computational Linear Algebra ex1
# By: Nick Space Cowboy

import numpy as np
import time

if __name__ == "__main__":
	s = time.time()
	print("A:")
	# Generates a random 10x10 matrix with values between zero to 100
	A = np.array(np.random.randint (0,100,(10,10)))
	print(A)
	print("")
	# Creates an 10d "vector" (array) of zeros
	b = np.zeros(10)
	# Changes the 6th value of the b vector to 3
	b[6] = 3
	print("b transpose: ")
	print(b.T)
	print("")
	# solves the linear system for the x vector
	x = np.linalg.solve(A,b)
	print("x:")
	print(x)
	print("")
	print("Ax=b Check: ")
	# prints out the checked solution by doing Ax to see if we get b
	print(A.dot(x))
	end = time.time()
	print("")
	print("Runtime: " + str(end - s) + " seconds")
