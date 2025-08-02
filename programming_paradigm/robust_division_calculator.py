def safe_divide(numerator, denominator) :

    try :
        num = float(numerator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try :
        denom = float(denominator)
    except :
        return "Error: Please enter numeric values only."
    
    try :
        result = num / denom
    except ZeroDivisionError :
        return("Error: Cannot divide by zero.")
    
    return f"The result of the division is {result}"