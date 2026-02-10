import numpy as np 
a=np.array([[1,2,3],
           [4,5,6]])
b=np.array([10,20,30])
res = a+b
print(res)
print("\n")


print("1-Dimension")
a1 = np.array([1, 2, 3])
print(a1)

print("0-Dimension")
a0 = np.array(5)
print(a0)

print("2-Dimension")
a2 = np.array([[4, 5, 6],
               [8, 9, 10],
               [1, 2, 3]])
print(a2)
print("\n")



# Vectorized vs Loop example
arr = np.random.rand(100)
# Vectorized
squared = arr ** 2
print(arr)
print(squared)
print("\n")


#Reshape
print("Reshaped matrix")
arr = np.arange(12)
reshaped = arr.reshape(3, 4)
print(reshaped)

a = np.array([[1, 2]])
print(a)
b = np.array([[3, 4]])
print(b)
print("\n")


#VStacked
print("Vertical Stack")
vstacked = np.vstack((a, b))
print(vstacked)

print("Horizontal Stack")
hstacked = np.hstack((a, b))
print(hstacked)
print("\n")



print("Statistical Function")
data = np.array([[10, 20, 30],
                 [40, 50, 60]])

print(np.mean(data))
print(np.mean(data, axis=0))
print(np.mean(data, axis=1))
print("\n")

print("Linear algebra")
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])
print(np.dot(A, B))


