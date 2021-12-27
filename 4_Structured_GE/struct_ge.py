# Computational Linear Algebra #4 Structured Gaussian Elimination
# By: Nick Space Cowboy

import numpy as np

class Cowboy_Lin_Alg(object):
	def solve_utri(self, Utri, b):
		n = len(Utri) # row dimension of the Utri matrix
		x = np.zeros_like(b, dtype=np.float64)
		for i in range(n - 1, -1, -1):	# loop to iterate through row index
			x[i] += b[i] / Utri[i,i]
			for j in range(n-1, i, -1):	# loop to iterate through the off diagonal Sum part
				x[i] += (- (Utri[i, j] * x[j])) / Utri[i,i]
		return x
		
	def SGE(self, Am, b):
		n = len(Am)
		l = np.zeros([n, n], dtype=np.float64)
		for i in range(0, n, 1):
			for j in range(i+1, n, 1):
				l[j,i] = A[j,i] / A[i,i]
				A[j] = A[j] - (l[j,i] * A[i])
				b[j] = b[j] - (l[j,i] * b[i])
		return A, b
			
if __name__ == "__main__":		
	A = np.array(np.random.randint (0,100,(4,4)), dtype=np.float64)
	Ac = A.copy()
	print("A = ")
	print(A)
	b = np.array(np.random.randint(0, 100, (4,1)), dtype=np.float64)	
	print("b = ")
	print(b)
	cla = Cowboy_Lin_Alg()
	cla.SGE(A,b)
	x = cla.solve_utri(A, b)
	print("U = ")
	print(A)
	print("c = ")
	print(b)
	print("x = ")
	print(x)
	print("Check Ax = ")
	print(Ac.dot(x))
