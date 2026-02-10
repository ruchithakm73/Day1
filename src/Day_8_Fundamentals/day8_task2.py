import numpy as np

data = np.arange(24)
print("Original 1D array:")
print(data)

reshaped = data.reshape(4, 3, 2)
print("\nReshaped to (4, 3, 2):")
print(reshaped)

transposed = reshaped.transpose(0, 2, 1)
print("\nTransposed to (4, 2, 3):")
print(transposed)

print("\nFinal Shape:")
print(transposed.shape)


