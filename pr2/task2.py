def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Ділення на 0"

def calculator(x, y, op):
    if op == "+":
        return add(x, y)
    elif op == "-":
        return subtract(x, y)
    elif op == "*":
        return multiply(x, y)
    elif op == "/":
        return divide(x, y)
    
print(calculator(5, 2, "+"))
print(calculator(5, 2, "/"))
print(calculator(5, 2, "-"))
print(calculator(5, 2, "*"))
