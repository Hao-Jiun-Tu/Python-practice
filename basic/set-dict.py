# SET & DICTIONARY

# set
s1 = {3, 4, 5}
print(3 in s1)       # True
print(10 not in s1)  # False

s1 = {3, 4, 5}
s2 = {4, 5, 6, 7}
s3 = s1 & s2
print("s3 =", s3) # {4, 5}
s4 = s1 | s2
print("s4 =", s4) # {3, 4, 5, 6, 7}
s5 = s1 - s2
print("s5 =", s5) # {3}
s6 = s1 ^ s2
print("s6 =", s6) # {3, 6, 7}

s = set("Hello") # string sets (not repeated)
print("H" in s)  # True
print("A" in s)  # False

# dictionary : key-value
dic = {"apple" : "fruit", "python" : "program"}
dic["apple"] = "iphone"
print(dic["apple"])
print("python" in dic) # True
del dic["python"]
print(dic)

dic = {x : x*2 for x in [3, 4, 5]}
print(dic)
