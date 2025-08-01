def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2 
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        return num1 / num2
        if num2 == 0 :
            print("We cant devide on 0 please choose another number")
    else:
        print("Please choose one of the mentioned operations!")