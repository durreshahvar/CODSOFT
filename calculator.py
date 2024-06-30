import random
def add(n1, n2, n3):
    return n1 + n2 + n3
def subtract(n1, n2, n3):
    return n1 - n2 - n3
def multiply(n1, n2, n3):
    return n1 * n2 * n3
def divide(n1, n2, n3):
    return n1 / n2 / n3
print("select operations")
print(
    "1. Add\n"
    "2. Subtract\n"
    "3. Multiply\n"
    "4. Divide\n")
operation = int(input("Enter choice of operation 1/2/3/4: "))
n1 = float(input("Enter the n1: "))
n2 = float(input("Enter the n2: "))
n3 = float(input("Enter the n3: "))
if operation == 1:
    print(n1, "+", n2, "+", n3, "=", add(n1, n2, n3))
elif operation == 2:
    print(n1, "-", n2, "-", n3, "=", subtract(n1, n2, n3))
elif operation == 3:
    print(n1, "", n2, "", n3, "=", multiply(n1, n2, n3))
elif operation == 4:
    print(n1, "/", n2, "/", n3, "=", divide(n1, n2, n3))
else: 
    print("Invalid Input")