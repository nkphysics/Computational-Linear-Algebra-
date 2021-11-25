# Computational Linear Algebra Ep#2 ex1
# By: Nick Space Cowboy

close all;
clear all;

b = randi(100, 10, 1) # generates random 10d b vector
A = randi(100, 10, 10)# genertates random 10x10 A matrix
tic
x = A\b
toc
utri = triu(randi(100, 10, 10),0) # generates random 10x10 upper triangular matrix
tic
x_tri = utri\b
toc
