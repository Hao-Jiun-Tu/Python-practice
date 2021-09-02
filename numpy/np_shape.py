# NUMPY-ARRAY-SHAPE
import numpy as np

# array data shape
data = np.ones(10)
print(data.shape) # (10,)
data = np.array([
    [3, 1, 5],
    [1, 2, 3]
]) # 2x3 array
print(data.shape)   # (2, 3)
print(data.T)    
print(data.T.shape) # (3, 2)
print("=======================")

data = np.array([
    [
        [2, 1, 3], [1, 2, 3]
    ],
    [
        [0, 2, 1], [8, 9, 10]
    ]
]) # 2x2x3 array
newData = data.ravel() # flatten the data
print(newData)
print(newData.shape) # (12,)

newData = data.reshape(3, 4) # reshape the data (3x4=12)
print(newData)
print(newData.shape) # (3, 4)
# newData = data.reshape(3, 5) # 3x5=15!=12 --> error
# print(newData)
print("=======================")

data = np.arange(9).reshape(3, 3)
print(data)
print(data.T)

