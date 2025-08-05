#Ask user first number
num1 = float(input("Enter first number:"))
#Ask user second number
num2 = float(input("Enter second number:"))
#Ask user mathematical operation
operation = input("Choose an operation (+, -, *, /): ")

# Perform the operation based on uer's feedback
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif operation == "/":
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
