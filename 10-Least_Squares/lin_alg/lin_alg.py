# Cowboy Linear Algebra python library at Video #9
# By: Nick the Space Cowboy

import numpy as np

def back_sub(Utri, c):
	'''
	back substitution alogrithm for solving upper triangular system
	'''
	m = len(Utri) # row dimension of the Utri matrix
	n = len(Utri[0]) # column dimension of the Utri matrix
	x = np.zeros([n, 1], dtype=np.float64)
	b = np.array(c, dtype=np.float64)
	t1 = 0
	if m > n:
		# ct1 = m
		# m = n
		raise Exception ("More rows than columns (Use a different method)")
	for i in range(m - 1, -1, -1):	# loop to iterate through row index
		x[i] += b[i] / Utri[i, i]
		for j in range(n - 1 , i, -1):	# loop to iterate through the off diagonal Sum part
			x[i] += (- (Utri[i, j] * x[j])) / Utri[i, i]
	return x
		
def SGE(A, b=0):
	'''
	function to perform structured gaussian elimination 
	If a b vector isn't passed through, a LU decomposition is returned
	'''
	m = len(A)
	n = len(A[0])
	L = np.identity(m, dtype=np.float64)
	U = np.array(A)
	c = np.array(b)
	b_state = isinstance(b, np.ndarray)
	for i in range(0, n, 1):
		for j in range(i+1, m, 1):
			L[j,i] = U[j,i] / U[i,i]
			U[j] = U[j] - (L[j,i] * U[i])
			if b_state == False:
				pass
			else:
				c[j] = c[j] - (L[j,i] * c[i])
	if b_state==False:
		return L, U
	else:
		return U, c
	
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
	m = len(A)
	n = len(A[0])
	D = np.identity(m, dtype=np.float64)
	for i in range(0, m, 1):
		for j in range(0, n, 1):
			if i == j: 
				D[i, j] = U[i, j]
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
	
def LDLT(A):
	'''
	Function to perform the LDL^T matrix decomposition
	'''
	C = cholesky(A)
	n = len(A)
	D = np.identity(n, dtype=np.float64)
	L = C
	for i in range(0, n):
		D[i, i] = C[i, i]**2
		L[:, i] = C[:, i] * D[i, i] ** (-1/2)
	return L, D

def least_squares(A, b):
	B = np.dot(A.T, A)
	d = np.dot(A.T, b)
	U, c = SGE(B, d)
	x = back_sub(U, c)
	norm = np.linalg.norm(b - np.dot(A, x))
	return x, norm
	
	
