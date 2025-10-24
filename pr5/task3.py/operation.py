from function import add, subtract, multiply, divide

def numbers():
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    return a, b

def perform_operation():
    print("Оберіть операцію: +, -, *, /")
    operation = input("Операція: ")

    a, b = numbers()

    if operation == '+':
        print(f"Результат: {add(a, b)}")
    elif operation == '-':
        print(f"Результат: {subtract(a, b)}")
    elif operation == '*':
        print(f"Результат: {multiply(a, b)}")
    elif operation == '/':
        print(f"Результат: {divide(a, b)}")
    else:
        print("Невідома операція")
