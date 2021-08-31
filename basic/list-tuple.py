# LIST & TUPLE

# list : data in list is changable
grades = [12, 60, 15, 70, 90]
grades[0:2] = [55, 44]
print(grades) # [55, 44, 15, 70, 90]
grades[3:5] = []
print(grades) # [55, 44, 15]
grades += [12, 33]
print(grades) # [55, 44, 15, 12, 33]
print("List of the length =", len(grades))

data = [[3, 4, 5], [6, 7, 8]]
data[0][0:2] = [5, 5, 5]
print(data)

# tuple : data in tuple is unchangable
data = (3, 4, 5)
#data[0] = 5  ==> error occurs
data += (6, 7, 8)
print(data)

