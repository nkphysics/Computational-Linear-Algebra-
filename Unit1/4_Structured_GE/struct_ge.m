# Computational Linear Algebra Ep#4 Structured Gaussian Elimination
# By: Nick Space Cowboy

clear all;
close all;

function x = solve_utri(A,b) # creates the function solve_utri
	n = length(b);	# To help with indexing
	x = zeros(n,1);	# creates a x vector to be filled
	for k=n:-1:2	# starts iterating through matrix 
		x(k) = b(k)/A(k,k);
		b(1:k-1) = b(1:k-1) - x(k)*A(1:k-1,k);
	end
	x(1) = b(1)/A(1,1);
endfunction

function [A,b] = sge(A,b) 
	# takes an input A matrix and b vector of a linear system
	# and converts the system to Ux=c through structured gaussian elimination
	n = length(b);
	L = zeros(n,n);
	for k=1:1:n
		for l=(k+1):1:n
			L(l,k) = A(l,k) / A(k,k); # get and store the multipliers
			A(l,:) = A(l,:) - (L(l,k) * A(k, :));# use the multipliers to zero out a position of A
			b(l) = b(l) - (L(l,k) * b(k)); # use the multipliers to change a value of b
		end
	end
endfunction


b = randi(100, 5, 1) # generates random b vector
A = randi(100, 5, 5)# genertates random A matrix
[U,c] = sge(A,b)# converts the system to Ux=c through SGE
x = solve_utri(U,c)	# solves the system with our created function

check = A*x	# checks that our result is in fact correct
