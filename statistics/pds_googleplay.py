# PANDAS DATA ANALYSIS - GOOGLE PLAY STORE DATA
import pandas as pd

# read data from .csv
data = pd.read_csv("googleplaystore.csv")
print(data)

print("Data-num:", data.shape)
print("Data-col:", data.columns)
print("=======================")
