# Computational Linear Algebra Ep#2 ex1
# By: Nick Space Cowboy

close all;
clear all;

b = randi(100, 10, 1)
A = randi(100, 10, 10)
tic
x = A\b
toc
utri = triu(randi(100, 10, 10),0)
tic
x_tri = utri\b
toc
