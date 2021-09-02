# NUMPY-NDARRAY
import numpy as np

# 1-D array
data = np.array([3, 2, 6, 4])
print(data)
data = np.empty(4) # data is not assigned
print(data)
data = np.zeros(3)
print(data)
data = np.ones(3)
print(data)
data = np.arange(5)
print(data)
print("=======================")

# 2-D array
data = np.array([  # 3x3 array
    [2, 3, 2],
    [1, 5, 2],
    [4, 2, 1]
])
print(data)
data = np.empty([3, 3]) # data is not assigned
print(data)
data = np.ones([2, 3])
print(data)
print("=======================")

# 3-D array
data = np.array([  # 2x2x2 array
    [
        [3, 1], [1, 2]
    ],
    [
        [2, 5], [10, 2]
    ]
])
print(data)
data = np.zeros([3, 1, 3])
print(data)
print("=======================")

# High-D array
data = np.ones([2, 1, 1, 2]) # 2x1x1x2 array, all data are assigned to 1
print(data)
