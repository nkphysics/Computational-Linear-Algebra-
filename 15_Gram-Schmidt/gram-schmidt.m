# Computational Linear Algebra Ep#15 Gram-Schmidt Process
# By: Nick Space Cowboy

clear all;
close all;

function Q = gram_schmidt(A)
    [n, k] = size(A);
    Q = zeros(n,k);
    Q(:,1) = A(:,1) / norm(A(:,1));
    for i = 2:k
        Q(:,i) = A(:,i);
        for j = 1:i-1
            Q(:,i) = Q(:,i) - (Q(:,j)'* Q(:,i)) * Q(:,j);
        end
        Q(:,i) = Q(:,i) / norm(Q(:,i));
    end
endfunction

function inner_products(M)
    [m, n] = size(M);
    for i = 2:n
        inner_product = dot(M(:,i-1), M(:, i))
    end
    inner_product = dot(M(:, 1), M(:, n))
endfunction

A = randi(10, 3, 3)
inner_products(A)
Q = gram_schmidt(A)
inner_products(Q)
check = Q * Q'
