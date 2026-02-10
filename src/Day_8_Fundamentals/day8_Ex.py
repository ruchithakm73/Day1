import numpy as np
# 1D Array
arr = np.array([1, 2, 3, 4, 5])
print("1D NumPy Array:", arr)
print("\n")
# 2D Array
arr_2d = np.array([[1, 2], [3, 4]])
print("2D NumPy Array:\n", arr_2d)
print("\n")
# 0D, 1D, 2D, 3D Arrays
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6],[7,8,9]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print("\n ",a)
print("\n",b)
print("\n",c)
print("\n",d)

print(a.ndim)  # 0D
print(b.ndim)  # 1D
print(c.ndim)  # 2D
print(d.ndim)  # 3D

arr=np.array([1,2,3,4,6,7])
print(arr.shape)

# Simple Indexing
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row:', arr[0, 1]) #arr[row,column]

# 3D Indexing
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[1, 0, 2]) # arr[axis,row,column]

# 1D Slicing
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

# Using arange (Start, Stop, Step)
arr = np.arange(40, 55, 3)
print("Array of numbers:", arr)
#two dimensional array
print(arr.shape)
arr_1 =np.arange(1,17).reshape(4,4)
print(arr_1)

#create 3d array using arange function
arr = np.arange(0, 12, 2)
print(arr)
print("Shape before reshape:", arr.shape)

arr3d = arr.reshape(1, 2, 3)
print("Shape after reshape:", arr3d.shape)
print(arr3d)

# Using linspace (Evenly spaced)
arr = np.linspace(0, 2, 5)
print(arr)

# Random values
arr = np.random.rand(2, 2)
print(arr)

import numpy as np

arr = np.random.randn(2, 3)
print(arr)

arr = np.random.uniform(20, 30, size=(2, 2))
print(arr)
print(arr.dtype)

arr = np.random.randint(10, 15, size=(3, 3))
print(arr)
print(arr.size)

# Array Inspection
arr = np.array([[1, 2], [3, 4]])
print(arr.shape)  # Shape (rows, columns)

arr = np.array([1, 2, 3])
print(arr.dtype)  # Data type

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.size)  # Total number of elements

#Array Operations & Broadcasting
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print("Addition:", a + b)  # Element-wise addition
print("Multiplication by scalar:", a * 2)
print("Element-wise multiplication:", a * b)
print("Mean of array a:", np.mean(a))

# Universal Functions (ufuncs)

arr = np.array([1, 4, 9])
print(np.sqrt(arr))  # Square root

arr = np.array([0, np.pi/2])
print(np.sin(arr))  # Sine

arr = np.array([1, 2])
print(np.exp(arr))  # Exponential

import numpy as np
arr = np.array([1.2, 2.8, -3.7])
print(np.floor(arr))
arr = np.array([1.2, 2.8, -3.7])
print(np.ceil(arr))
print("trunc",np.trunc(arr))#removes only the decimal
print("round",np.round(arr))

arr = np.array([1, np.e, np.e**2])
print(np.log(arr))

