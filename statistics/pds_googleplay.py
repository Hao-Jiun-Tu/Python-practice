# PANDAS DATA ANALYSIS - GOOGLE PLAY STORE DATA
import pandas as pd

# read data from .csv
data = pd.read_csv("googleplaystore.csv")
print(data)

print("Data-num:", data.shape)
print("Data-col:", data.columns)
print("=======================")

# condition = (data["Rating"] > 5)
# target = data[condition]
# print(data)
condition = (data["Rating"] <= 5)
target = data[condition]
print("Avg:", target["Rating"].mean())
print("Median:", target["Rating"].median())
print("The first hundred avg:", target["Rating"].nlargest(100).mean())

# print(data["Installs"])
print(data["Installs"][10472]) # print out "Free" --> garbage data
data["Installs"] = pd.to_numeric(data["Installs"].str.replace("[,+]", "").replace("Free", ""))
print(data["Installs"])
condition = (data["Installs"] > 100000)
print("Installing quantities larger than 1000000", data[condition].shape[0])

keyword = input("Please enter the keyword: ")
condition = data["App"].str.contains(keyword, case = False)
print("The number of App containing keyword:", data[condition].shape[0])