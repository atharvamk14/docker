import numpy as np

# Define the 3x3 matrix
matrix1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Define the 3x6 matrix
matrix2 = np.array([
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18]
])

# Multiply the matrices
result = np.dot(matrix1, matrix2)

# Display the result
print("Result of the multiplication:")
print(result)