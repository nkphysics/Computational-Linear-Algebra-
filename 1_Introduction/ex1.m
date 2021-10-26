clear all;

# Generates a random 10x10 matrix with non-zero ints up to 100
A = randi(100, 10, 10) 

# Creates a 10-d column vector of zeros
b = zeros(1,10)';
# Makes the 6th element of the b vector 3
b(6) = 3

# Solves Ax=b for x and times how long it takes
tic
x = A\b
toc
