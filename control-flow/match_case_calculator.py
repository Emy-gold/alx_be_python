num1 = input("Enter the first number:")
num2 = input("Enter the second number:")
operation = input("Choose the operation (+, -, *, /):")
if operation == "+":
    result = float(num1) + float(num2)
    print("The result is", result)
elif operation == "-":
    result = float(num1) - float(num2)
    print("The result is", result)
elif operation == "*":
    result = float(num1) * float(num2)
    print("The result is", result)
elif operation == "/":
    result = float(num1) / float(num2)
    print("The result is", result)
    if float(num2) == 0:
        result = "Cannot divide by zero"
    print("The result is", result)
else:
    result = "Invalid operation"