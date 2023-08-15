# LOGIC
# Create functions for add, subtract, multiply and divide
# Get user input
# Call functions
# Diplay values
# Run until exit is initiated

def get_operation():
    this_operation = input("Would you like to add, subtract, divide, or multiply?\nEnter 'e' to exit: ").strip()
    if this_operation == "e" or this_operation == "E":
        return "e"
    elif this_operation == "add" or this_operation == "+":
        return "+"
    elif this_operation == "subtract" or this_operation == "-":
        return "-"
    elif this_operation == "divide" or this_operation == "/":
        return "/"
    elif this_operation == "multiply" or this_operation == "*":
        return "*"
    else:
        print("Invalid input")
        return "continue"

def add(x, y):
    return float(x)+float(y)


def subtract(x, y):
    return float(x)-float(y)


def divide(x, y):
    try:
        return float(x) / float(y)
    except ZeroDivisionError:
        y = 1
        print("Cannot divide by zero")
        return float(x) / float(y)


def multiply(x, y):
    return float(x)*float(y)


while True:
    operation = get_operation()
    if operation == "e" or operation == "E":
        break
    elif operation == "continue":
        continue
    else:
        try:
            numbers = input("What two numbers would you like to calculate? Separate by a space: ")
            x, y = numbers.split()
        except ValueError:
            print("Please enter only two numbers, separated by a space")
            continue
        if operation == "+":
            print(add(x,y))
        elif operation == "-":
            print(subtract(x,y))
        elif operation == "/":
            print(divide(x,y))
        elif operation == "*":
            print(multiply(x,y))
        else:
            print("Invalid input")
