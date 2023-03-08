# Create a simple calculator that takes user input for two numbers and performs basic arithmetic
# operations such as addition, subtraction, multiplication, and division.
# Author: Chris K.

print("Welcome to Simple Calculator v1!")
while True:
    print("Enter your equation below using the operators +  -  /  *. (Please include spaces!)")
    equation = input()
    num_1, operator, num_2 = equation.split()
    num_1, num_2 = int(num_1), int(num_2)

    if operator == "+":
        print(f"{num_1} + {num_2} = {num_1 + num_2}")
    elif operator == "-":
        print(f"{num_1} - {num_2} = {num_1 - num_2}")
    elif operator == "/":
        print(f"{num_1} / {num_2} = {num_1 / num_2}")
    elif operator == "*":
        print(f"{num_1} * {num_2} = {num_1 * num_2}")
