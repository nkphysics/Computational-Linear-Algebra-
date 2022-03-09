# Cowboy Linear Algebra python library at Video #7
# By: Nick the Space Cowboy

import numpy as np

def back_sub(Utri, b):
	# back substitution alogrithm for solving upper triangular system
	n = len(Utri) # row dimension of the Utri matrix
	x = np.zeros_like(b, dtype=np.float64)
	for i in range(n - 1, -1, -1):	# loop to iterate through row index
		x[i] += b[i] / Utri[i,i]
		for j in range(n-1, i, -1):	# loop to iterate through the off diagonal Sum part
			x[i] += (- (Utri[i, j] * x[j])) / Utri[i,i]
	return x
		
def SGE(A, b=None):
	'''
	function to perform structured gaussian elimination 
	If a b vector isn't passed through, a LU decomposition is returned
	'''
	n = len(A)
	L = np.identity(n, dtype=np.float64)
	for i in range(0, n, 1):
		for j in range(i+1, n, 1):
			L[j,i] = A[j,i] / A[i,i]
			A[j] = A[j] - (L[j,i] * A[i])
			if b == None:
				pass
			else:
				b[j] = b[j] - (L[j,i] * b[i])
	if b==None:
		return L, A
	else:
		return A, b
	
def LU(A):
	'''
	Function to perform LU decomposition
	'''
	return SGE(A)
	
def LDV(A):
	'''
	Function to perform a LDV Matrix decomposition
	'''
	L, U = LU(A)
	n = len(A)
	D = np.identity(n, dtype=np.float64)
	for i in range(0, n, 1):
		D[i, i] = U[i, i]
	V = np.dot(np.linalg.inv(D), U)
	return L, D, V
	
def pos_def_check(A):
	'''
	Checks if a matrix is positive definate
	'''
	pd_state = True
	n = len(A)
	for i in range(1, n):
		if (A[i, i - 1] ** 2) >= A[i, i]:
			raise Exception ("Marix is not positive definate")
			pd_state =  False
	return pd_state
	
def cholesky(A):
	'''
	Function to perform a Cholesky decompostion
	'''
	pd = pos_def_check(A)
	if pd == True:
		n = len(A)
		L = np.zeros_like(A, dtype=np.float64)
		for i in range(0, n):
			for j in range(0, i + 1):
				sum_part = 0
				if i == j:
					for k in range(0, j):
						sum_part += L[j, k] ** 2
					L[i, j] = np.sqrt(A[j, j] - sum_part)
				else:
					for k in range(0, j):
						sum_part += L[i, k] * L[j, k]
					L[i, j] = (A[i, j] - sum_part) / L[j, j]
	else:
		L = f"Matrix is not positive definate"
	return L
