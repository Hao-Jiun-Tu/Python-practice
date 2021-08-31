# CONDITIONS

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
op = input("Enter operator: +, -, *, /: ")

if op == "+":
    print(n1 + n2)
elif op == "-":
    print(n1 - n2)
elif op == "*":
    print(n1 * n2)
elif op == "/":
    print(n1 / n2)
else:
    print("Not supported operator!")

