# PANDAS-BASIC
import pandas as pd

# Series
data = pd.Series([20, 10, 15])
print(data)
print("=======================")
print("Max", data.max())
print("Median", data.median())
print("=======================")
data = data * 2
print(data)
print("=======================")
data = (data == 20)
print(data)
print("=======================")

# DataFrame : save as a dictionary
data = pd.DataFrame({
    "name" : ["Amy", "John", "Bob"],
    "salary": ["30000", "50000", "40000"]
})
print(data)
print("=======================")
print(data["name"]) # print the "name" column
print("=======================")
print(data.iloc[0]) # print row index "0" 
