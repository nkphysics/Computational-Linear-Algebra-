# Computational Linear Algebra Ep#3 Uppper Triangle Algorithm
# By: Nick Space Cowboy

import numpy as np

class Cowboy_Lin_Alg(object):
	def solve_utri(self, Utri, b):
		n = len(Utri) # row dimension of the Utri matrix
		x = np.zeros_like(b, dtype=float)
		for i in range(n - 1, -1, -1):	# loop to iterate through row index
			x[i] += b[i] / Utri[i,i]
			for j in range(n-1, i, -1):	# loop to iterate through the off diagonal Sum part
				x[i] += (- (Utri[i, j] * x[j])) / Utri[i,i]
		return x
		
			
if __name__ == "__main__":
	cla = Cowboy_Lin_Alg()
	A = np.array(np.random.randint (0,100,(4,4)))
	U = np.triu(A)
	print("U: " + str(U))
	b = np.array(np.random.randint(0, 100, (4,1)))
	print("b:" + str(b))
	x = cla.solve_utri(U,b)
	print("x: " + str(x))
	print("Check: " + str(U.dot(x)))
	
