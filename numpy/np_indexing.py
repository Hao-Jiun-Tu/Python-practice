# NUMPY-ARRAY-INDEXING
import numpy as np

# array index
data = np.array([1, 5, 2, 10])
print(data[1]) # 5
print("=======================")

data = np.array([
    [0, 1],
    [10, -5],
    [2, 6]
])
print(data[0, 1]) # 1
print(data[1, 0]) # 10
print(data[2, 0]) # 2
print("=======================")

# array slicing
data = np.array([-1, -5, 2, 3])
print(data[0:3]) # [-1, -5 , 2]
print(data[:2])  # [-1, -5]
print(data[2:])  # [2, 3]
print(data[:])   # [-1, -5, 2, 3]
print("=======================")

data = np.array([
    [0, 1, 2], [3, 4, 5],
    [5, 4, 3], [2, 1, 0]
])
print(data[1:3, 0:2]) # [[3, 4], [5, 4]]
print(data[0:2, 1])   # [1, 4]
print("=======================")

data = np.array([
    [
        [8, 1, 3], 
        [-5, 5, 2]
    ],
    [
        [0, 1, 6],
        [4, 4, -3]
    ]
])
print(data[0, ...])   # [[8, 1, 3], [-5, 5, 2]]
print("=======================")
print(data[..., 1:3]) # [[[1, 3], [5, 2]], [[1, 6], [4, -3]]]

