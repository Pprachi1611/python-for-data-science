import numpy as np

# Reshape
arr = np.arange(12)
reshaped = arr.reshape(3, 4)

# Flatten
flat = reshaped.flatten()

# Random numbers
rand = np.random.rand(3, 3)

# Boolean masking
data = np.array([10, 20, 30, 40])
filtered = data[data > 20]

print(reshaped)
print(flat)
print(rand)
print(filtered)