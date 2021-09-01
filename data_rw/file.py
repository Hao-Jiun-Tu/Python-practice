# FILE HANDLE
# save file 1
file = open("data1.txt", mode = "w", encoding = "utf-8")
file.write("Hello World")
file.close

# save file 2
with open("data2.txt", mode = "w", encoding = "utf-8") as FILE:
    FILE.write("5\n3\n6\n10")

# read file 2
with open("data2.txt", mode = "r", encoding = "utf-8") as FILE:
    data = FILE.read()
print(data)

# summation
sum = 0
with open("data2.txt", mode = "r", encoding = "utf-8") as FILE:
    for line in FILE:
        sum += int(line)
print(sum)

# Read JSON file
import json
with open("config.json", mode = "r") as FILE:
    data = json.load(FILE)
print(data) # data type = dictionary
print("name:", data["name"])
print("version", data["version"])

# Write JSON file
data["name"] = "Hao-Jiun-Tu"
with open("config.json", mode = "w") as FILE:
    json.dump(data, FILE)

