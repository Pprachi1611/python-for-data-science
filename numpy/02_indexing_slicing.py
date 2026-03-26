import numpy as np

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

# Access elements
print(arr[0, 1])

# Row
print(arr[1, :])

# Column
print(arr[:, 1])

# Sub-matrix
print(arr[0:2, 1:3])