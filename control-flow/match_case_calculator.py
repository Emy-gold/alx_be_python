num1 = input("Enter the first number:")
num2 = input("Enter the second number:")
operation = input("Choose the operation (+, -, *, /)")
if operation == "+":
    result = float(num1) + float(num2)
elif operation == "-":
    result = float(num1) - float(num2)
elif operation == "*":
    result = float(num1) * float(num2)
elif operation == "/":
    result = float(num1) / float(num2)
    if float(num2) == 0:
        result = "Cannot divide by zero"
else:
    result = "Invalid operation"