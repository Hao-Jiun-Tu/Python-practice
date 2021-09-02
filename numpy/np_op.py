# NUMPY-ARRAY-OPERATIONS
import numpy as np

# elementwise op
data1 = np.array([3, 2, 10])
data2 = np.array([1, 3, 6])
result = data1 + data2
print("Add:", result)
result = data1 * data2
print("Mult:", result)
result = (data1 > data2)
print("Largest:", result)
result = (data1 == data2)
print("Equal:", result)
print("=======================")

# matrix op
data1 = np.array([
    [1, 3]
]) # 1x2
data2 = np.array([
    [2, -1, 3],
    [-2, 4, 1]
]) # 2x3
result = data1.dot(data2)
print("Inner-product:", result)
result = np.outer(data1, data2)
print("Outer-product:", result)
print("=======================")

# statistics
data = np.array([
    [2, 1, 7],
    [-5, 3, 8]
])
result = data.sum()
print("Sum:", result)
result = data.max()
print("Max:", result)
result = data.mean()
print("Mean:", result)
result = data.std()
print("Std:", result)
print("=======================")
result = data.sum(axis = 0) # summation for the first dimension
print(result)
result = data.sum(axis = 1) # summation for the second dimension
print(result)
result = data.max(axis = 0) # find the maximum for the first dimension
print(result)
 