from function import add, subtract, multiply, divide
from operation import get_numbers, get_operation
from logger import write_log

def main():
    a, b = get_numbers()
    op = get_operation()

    if op == '+':
        result = add(a, b)
    elif op == '-':
        result = subtract(a, b)
    elif op == '*':
        result = multiply(a, b)
    elif op == '/':
        result = divide(a, b)
    else:
        print("Невідома операція")
        return

    write_log(a, b, op, result)
    print(result)


if __name__ == "__main__":
    main()
