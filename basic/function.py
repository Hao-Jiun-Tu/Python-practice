# FUNCTION

def calculate(max):
    sum = 0
    for n in range(1, max):
        sum += n
    return sum

print("1+2+...+10 =", calculate(10))
print("1+2+...+20 =", calculate(20))

def power(base, exp=0):
    print(base ** exp)
power(3, 2) # = 9
power(4)    # = 1

def avg(*num): # num sent as tuple
    sum = 0
    for n in num:
        sum += n
    print(sum / len(num))
avg(3, 4)
avg(3, 5, 10)
avg(1, 4, -1, -8)

