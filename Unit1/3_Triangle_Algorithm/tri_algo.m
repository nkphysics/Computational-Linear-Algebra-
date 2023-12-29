# Computational Linear Algebra Ep#3 Uppper Triangle Algorithm in Octave
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

b = randi(100, 10, 1) # generates random 10d b vector
A = triu(randi(100, 10, 10),0)# genertates random 10x10 A matrix
x = solve_utri(A,b)	# solves the system with our created function

check = A*x	# checks that our result is in fact correct
