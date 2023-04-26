#write a calculator program using functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


# Get user input for two numbers
x = float(input("Enter first number: "))

choice=(input("select operation--> +,-,*,/:-->  ")) #select operation

y = float(input("Enter second number: "))


# Perform selected operation and print result
if choice == '+':
    print(x, "+", y, "=", add(x,y))

elif choice == '-':
    print(x, "-", y, "=", subtract(x,y))

elif choice == '*':
    print(x, "*", y, "=", multiply(x,y))

elif choice == '/':
    print(x, "/", y, "=", divide(x,y))

else:
    print("Invalid input")














