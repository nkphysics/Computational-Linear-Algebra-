# Computational Linear Algebra Ep#7 Cholesky Decomposition
# By: Nick Space Cowboy
clear all;
close all;

A = [randi(100), 5, 4;
	 5, randi(100), 9;
	 4, 9, randi(100)]
L = chol(A)'
check = L * L'
