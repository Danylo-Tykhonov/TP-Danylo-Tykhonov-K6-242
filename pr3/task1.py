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
            return "Невідома операція!"

def res():
    print("Калькулятор запущено. Введи 'exit' щоб завершити.")
    while True:
        a = input("Введи перше число: ")
        if a.lower() == "exit":
            print("Вихід з програми.")
            break

        b = input("Введи друге число: ")
        if b.lower() == "exit":
            print("Вихід з програми.")
            break

        op = input("Введи операцію (+, -, *, /): ")
        if op.lower() == "exit":
            print("Вихід з програми.")
            break

        try:
            a = float(a)
            b = float(b)
            result = calculator(a, b, op)
            print(f"Результат: {result}")
        except ValueError:
            print("Помилка!")

res()
