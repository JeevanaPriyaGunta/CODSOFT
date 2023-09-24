# Simple Calculator in Python

# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# User input
while True:
    print("Options:")
    print("Enter '1' for addition")
    print("Enter '2' for subtraction")
    print("Enter '3' for multiplication")
    print("Enter '4' for division")
    print("Enter '5' to end the program")

    choice = input("Enter operation: ")

    if choice == "quit":
        break

    if choice in ("1", "2", "3", "4"):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if choice == "1":
            print("Result: ", add(num1, num2))
        elif choice == "2":
            print("Result: ", subtract(num1, num2))
        elif choice == "3":
            print("Result: ", multiply(num1, num2))
        elif choice == "4":
            result = divide(num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                print("Result: ", result)
        else:
            print("Invalid input")
    else:
        print("Invalid input")