def plus(a: int | float, b: int | float):
    return float(a) + float(b)

def minus(a: int | float, b: int | float):
    return float(a) - float(b)

def multiply(a: int | float, b: int | float):
    return float(a) * float(b)

def divide(a: int | float, b: int | float):
    try:
        return float(a) / float(b)
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."