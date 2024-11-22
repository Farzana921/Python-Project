# task 2 Calculator
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

while True:
    operation = int(input("Enter the choice from (1,2,3,4,5): "))
    if operation in (1, 2, 3, 4, 5):
        if operation == 1:
            print("Addition of two numbers", number1, "and", number2, "is: ", add(number1, number2))
            print("--------------------------")
        elif operation == 2:
            print("Subtraction of two numbers", number1, "and", number2, "is: ", subtract(number1, number2))
            print("--------------------------")
        elif operation == 3:
            print("Multiplication of two numbers", number1, "and", number2, "is: ", multiply(number1, number2))
            print("--------------------------")
        elif operation == 4:
            print("Division of two numbers", number1, "and", number2, "is: ", divide(number1, number2))
            print("--------------------------")
        elif operation == 5:
            print("Goodbye")
            print("Thank you!")
            exit()
    else:
        print("Invalid choice, try again.")


