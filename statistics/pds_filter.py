# PANDAS-FILTER
import pandas as pd

# Series
data = pd.Series([30, 15, 20])
condition = (data > 18)
print(condition)
filteredData = data[condition]
print(filteredData)
print("=======================")

data = pd.Series(["Hello", "world", "PYTHON"])
condition = data.str.contains("P")
filteredData = data[condition]
print(filteredData)
print("=======================")

# DataFrame
data = pd.DataFrame({
    "name" : ["Amy", "John", "Bob"],
    "salary": [30000, 50000, 40000]
})
print(data)
print("=======================")
condition = (data["salary"] >= 40000)
filteredData = data[condition]
print(filteredData)
print("=======================")

condition = (data["name"] == "Amy")
filteredData = data[condition]
print(filteredData)