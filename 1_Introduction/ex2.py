import numpy as np
import time

if __name__ == "__main__":
	s = time.time()
	A = np.array(np.random.randint (0,1000000,(1000,1000)))
	b = np.zeros(1000)
	b[69] = 12
	x = np.linalg.solve(A,b)
	print("Ax=b Check for place 69: ")
	print(A.dot(x)[69])
	end = time.time()
	print("")
	print("Runtime: " + str(end - s) + " seconds")
