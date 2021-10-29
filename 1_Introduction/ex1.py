import numpy as np
import time

if __name__ == "__main__":
	s = time.time()
	print("A:")
	A = np.array(np.random.randint (0,100,(10,10)))
	print(A)
	print("")
	b = np.zeros(10)
	b[6] = 3
	print("b transpose: ")
	print(b.T)
	print("")
	x = np.linalg.solve(A,b)
	print("x:")
	print(x)
	print("")
	print("Ax=b Check: ")
	print(A.dot(x))
	end = time.time()
	print("")
	print("Runtime: " + str(end - s) + " seconds")
