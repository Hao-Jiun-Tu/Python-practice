# PANDAS-DATAFRAME
import pandas as pd

# DataFrame : save as a dictionary
data = pd.DataFrame({
    "name" : ["Amy", "John", "Bob"],
    "salary": [30000, 50000, 40000]
}, index = ["a", "b", "c"])
print(data)
print("=======================")

print("Data-num:", data.size)
print("Data-shape:", data.shape)
print("Data-index:", data.index)
print("=======================")

print("Row 2:", data.iloc[1], sep = "\n")
print("=======================")
print("Row \"c\":", data.loc["c"], sep = "\n")
print("=======================")

print("Col \"name\":", data["name"], sep = "\n")
names = data["name"]
print("All names to upper-case:", names.str.upper(), sep = "\n")
salaries = data["salary"]
print("The average to salaries:", salaries.mean())
print("=======================")

data["revenue"] = [500000, 400000, 300000]
data["rank"] = pd.Series([3, 6, 1], index = ["a", "b", "c"])
data["cp"] = data["revenue"] / data["salary"]
print(data)
