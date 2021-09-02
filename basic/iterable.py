# ITERABLE DATA TYPE
# string, list, set, dictionary

# for loop
# for variable in iterable-data
for x in "abc":
    print(x)

for x in [5, 10, 75]:
    print(x)

for x in {5, 9, 7}:
    print(x)

dic = {"j" : "Jason", "a" : "Alice"}
for key in dic:
    print(key)
    print(dic[key])

# functions
# max(iterable-data)
# sorted(iterable-data)
result = max("abc")
print(result)

result = max([5, 10, 75])
print(result)

result = sorted({5, 9, 7})
print(result)

dic = {"j" : "Jason", "a" : "Alice"}
result = sorted(dic)
print(result)