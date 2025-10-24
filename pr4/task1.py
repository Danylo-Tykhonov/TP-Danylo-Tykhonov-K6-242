def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        return "Помилка: ділення на нуль!"

def calculator(x, y, op):
    try:
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
    except Exception as e:
        return f"Сталася помилка: {e}"

def run_calculator():
    print("Калькулятор запущено. Введи 'exit' щоб завершити.")
    while True:
        try:
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

            a = float(a)
            b = float(b)

            result = calculator(a, b, op)
            print(f"Результат: {result}")

        except ValueError:
            print("Помилка: введено не число!")
        except Exception as e:
            print(f"Невідома помилка: {e}")

run_calculator()
