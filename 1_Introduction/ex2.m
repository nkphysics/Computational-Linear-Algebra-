# Computational Linear Algebra ex2
# By: Nick Space Cowboy

clear all;
# Does the same thing as ex1.m except only x is output

# Generates a random 1000x1000 matrix with non-zero ints up to 1,000,000
A = randi(1000000, 1000, 1000);

# Creates a 1000-d column vector of zeros
b = zeros(1,1000)';
# Makes the 6th element of the b vector 3
b(69) = 12;

# Solves Ax=b for x and times how long it takes + confirms it
tic
x = A\b;
c = A*x;
c(69)
toc
