def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ділення на 0!"
    return x / y

def calculator(x, y, op):
    match op:
        case "+":
            return add(x, y)
        case "-":
            return subtract(x, y)
        case "*":
            return multiply(x, y)
        case "/":
            return divide(x, y)
        case _:
            return "Неизвестная операция"

print(calculator(5, 2, "*"))
print(calculator(5, 0, "/"))
print(calculator(5, 2, "+"))
print(calculator(5, 2, "-"))
