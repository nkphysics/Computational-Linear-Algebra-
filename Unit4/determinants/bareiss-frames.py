import numpy as np
import matplotlib.pyplot as plt

frames = []

def bareiss(A: np.ndarray):
    # Get the dimensions of the matrix
    m, n = np.shape(A)
    sign = 1
    
    # Check if the matrix is square; raise an error if not
    if m != n:
        raise TypeError("Matrix is not square")
    
    # Initialize the sign factor to 1 (or -1 for a row swap)
    for k in range(n - 1):
        # Iterate through columns
        if A[k][k] == 0:
            # If a zero is on the diagonal
            for l in range(k + 1, n):
                if A[l][k] != 0:
                    # Swap the two rows
                    A[l], A[k] = A[k], A[l]
                    # Update the sign factor (since we swapped a row)
                    sign = -sign
                    break
            # If we reached this point and didn't swap rows, the matrix is singular
            # so the determinant of the matrix will be zero
            if (l == n - 1):
                return 0            
        # Subtract multiples of one column from others to eliminate 
        # columns below the diagonal
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = A[k][k] * A[i][j] - A[i][k] * A[k][j]
                # If we're not at the top row yet, divide rows below by the pivot element
                if k != 0:
                    A[i][j] = A[i][j] // A[k - 1][k - 1]
        frames.append(A.copy())
    # The determinant the sign factor times the last diagonal element
    return (sign * A[n - 1][n - 1])


if __name__ == "__main__":
    B = np.random.randint(-20, 21, size=(8, 8), dtype=np.int64)
    bareiss_det = bareiss(B)

    plt.style.use("dark_background")
    for num, frame in enumerate(frames):
        fig, a = plt.subplots()
        a.imshow(frame)
        a.set_title(f"Bareiss Pass #{num + 1}")
        plt.savefig(f"bareiss-{num}.jpg")
