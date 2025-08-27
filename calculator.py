#  Simple Calculator Program
import math as m

# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract second number  from first
def subtract(a, b):
    return a - b

#  Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide first number by second
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
    
#  Function to calculate square root of number
def square_root(num):
    return m.sqrt(num)

#  Function to calculate exponentiation function to raise first number to the power of second
def exponent(a, b):
    return m.pow(a, b)

#  Display operation options to the user
print("==== Select operation ====")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square root")
print("6. Exponential")
print("0. Exit")


while True:

    #  Take input from the user for operation choice
    choice = input("Enter choice (1/2/3/4): ")

    #  Get two numbers as input from the user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    #  Perform calculations based on user's choice
    if choice == "1":
        print("Result:", add(num1, num2))
    elif choice == "2":
        print("Result:", subtract(num1, num2))
    elif choice == "3":
        print("Result:", multiply(num1, num2))
    elif choice == "4":
        print("Result:", divide(num1, num2))
    elif choice == "5":
        print(f"Result for square of {num1}: {square_root(num1)}")
        print(f"Result for square of {num2}: {square_root(num2)}")
    elif choice == "6":
        print("Result:", exponent(num1, num2))
    elif choice == "0":
        break
    else:
        print("Invalid choice!")