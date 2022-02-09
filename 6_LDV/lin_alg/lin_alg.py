# Cowboy Linear Algebra python library at Video #5
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
	# function to perform structured gaussian elimination 
	# If a b vector isn't passed through, a LU decomposition is returned
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
	# Function to perform LU decomposition
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
