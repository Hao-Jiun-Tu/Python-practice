# LOOP

# while loop
n = 1
sum = 0
while n <= 10:
    sum += n
    n += 1
print(sum)

# for loop
for x in [3, 5, 1]:
    print(x)

for x in "Hello":
    print(x)

sum = 0
for x in range(1, 11):
    sum += x
print(sum)

# finding sqrt root of a number
n = int(input("Enter a positive number: "))
for i in range(1, n):
    if i*i == n:
        print("Sqrt root:", i)
        break # won't execute else part
else:
    print("No sqrt root!")

