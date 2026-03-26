import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

# Arithmetic
print("Addition:", a + b)
print("Multiplication:", a * b)

# Broadcasting
print("Add scalar:", a + 10)

# Matrix multiplication
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

print("Dot Product:\n", np.dot(A, B))