# Computational Linear Algebra ex2
# By: Nick Space Cowboy

import numpy as np
import time

if __name__ == "__main__":
	s = time.time()
	# Generates a random 1000x1000 matrix with values between zero to 1 million
	A = np.array(np.random.randint (0,1000000,(1000,1000)))
	b = np.zeros(1000)
	# Changes the 69th value of the b vector to 12
	b[69] = 12
	# Solves the system for the x vector
	x = np.linalg.solve(A,b)
	print("Ax=b Check for place 69: ")
	# Computes Ax to verify the solution is correct
	print(A.dot(x)[69])
	end = time.time()
	print("")
	print("Runtime: " + str(end - s) + " seconds")
