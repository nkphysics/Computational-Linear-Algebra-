# Computational Linear Algebra Ep#5 LU Decomposition
# By: Nick Space Cowboy

clear all;
close all;

function [L, U] = LU(A) 
	# takes an input A matrix decomposes it into a lower and upper triangular matrix
	n = length(A)
	L = eye(n,n);
	for k=1:1:n
		for l=(k+1):1:n
			L(l,k) = A(l,k) / A(k,k); # get and store the multipliers
			A(l,:) = A(l,:) - (L(l,k) * A(k, :));# use the multipliers to zero out a position of A
		end
		U = A;
	end
endfunction

A = randi(100, 5, 5)# genertates random A matrix
[L, U] = LU(A)# Exctacts a lower and upper triangular matrix with our created LU function
check = L*U	# checks that our result is in fact correctly
