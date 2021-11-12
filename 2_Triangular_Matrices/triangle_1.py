import numpy as np
import time

if __name__ == "__main__":
	print("A:")
	# Generates a random 10x10  upper triangular matrix with values between zero to 100
	A = np.array(np.random.randint (0,100,(10,10)))
	A1 = np.triu(A)
	print(A)
	print("A1:")
	print(A1)
	print("")
	b = np.array(np.random.randint(0, 100, (10,1)))
	print("b: ")
	print(b)
	print("")
	s1 = time.time()
	# Solve the normal A matrix system
	x = np.linalg.solve(A,b)
	s1e = time.time()
	print("x:")
	print(x)
	print("Full A matrix time: " + str(s1e - s1))
	s2 = time.time()
	# Solve the Triangular matrix system
	x1 = np.linalg.solve(A1,b)
	s2e = time.time()
	print("x1:")
	print(x1)
	print("Triangle matrix time: " + str(s2e - s2))
