def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiply")
    print("4. Division")
    print("5. Modulus")
    print("6. Floor division")

    # get the user's choice of operation
    choice = input("Enter choice of operation (+,-,*,/,%,//): ")

    # get the user's input for the numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # perform the selected operation based on the user's choice
    if choice == "+":
        result = num1 + num2
    elif choice == "-":
        result = num1 - num2
    elif choice == "*":
        result = num1 * num2
    elif choice == "/":
        result = num1 / num2
    elif choice == "%":
        result = num1 % num2
    elif choice == "//":
        result = num1 // num2
    else:
        print("Invalid input")
        exit()

    # display the result of the operation to the user
    print(num1, choice, num2, '= ', result)

# Call the calculator function
calculator()

# Define functions for arithmetic operations
def add():
    value1 = int(input("Enter first number: "))
    value2 = int(input("Enter second number: "))
    result = value1 + value2
    print("Result = ", result)

def subtraction():
    value1 = int(input("Enter first number: "))
    value2 = int(input("Enter second number: "))
    result = value1 - value2
    print("Result = ", result)

def multiply():
    value1 = int(input("Enter first number: "))
    value2 = int(input("Enter second number: "))
    result = value1 * value2
    print("Result = ", result)

def division():
    value1 = int(input("Enter first number: "))
    value2 = int(input("Enter second number: "))
    result = value1 / value2
    print("Result = ", result)

def modulus():
    value1 = int(input("Enter first number: "))
    value2 = int(input("Enter second number: "))
    result = value1 % value2
    print("Result = ", result)

def floor_division():
    value1 = int(input("Enter first number: "))
    value2 = int(input("Enter second number: "))
    result = value1 // value2
    print("Result = ", result)

# Call the arithmetic functions
add()
subtraction()
multiply()
division()
modulus()
floor_division()