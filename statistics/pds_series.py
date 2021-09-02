# PANDAS-SERIES
import pandas as pd

# Series
data = pd.Series([5, 4, -2, 3, 7], index = ["a", "b", "c", "d", "e"])
print(data)
print("=======================")

print("Data-type:", data.dtype)
print("Data-num:", data.size)
print("Data-index:", data.index)
print("=======================")

print(data[2], data[0])
print(data["e"], data["d"])
print("=======================")

print("Max:", data.max())
print("Sum:", data.sum())
print("Std:", data.std())
print("Median:", data.median())
print("3_largest:", data.nlargest(3))
print("3_smallest:", data.nsmallest(3))
print("=======================")

data = pd.Series(["Hello", "world", "PYTHON"])
print(data.str.lower())
print(data.str.upper())
print(data.str.len())
print(data.str.cat(sep = "-"))
print(data.str.contains("P"))
print(data.str.replace("world", "jason"))