import operation
import function
print("Calculator Program")
print("Enter 'q' at any time to leave\n")

while True:
    a = operation.getNumber("Enter the first number: \n")
    if a == 'Q' or a == 'q':
        operation.log('q')
        print("You left the program")
        break
    
    b = operation.getNumber("Enter the second number: \n")
    if b == 'Q' or b == 'q':
        operation.log('q')
        print("You left the program")
        break
    
    op = operation.getOperations("Choose an operation (+, -, *, /): \n")
    if op == 'Q' or op == 'q':
        operation.log('q')
        print("You left the program")
        break
    
    if op == '+':
        result = function.plus(a, b)
        operation.log(a, b, op, result)
        print(f"Answer: {result}")
    elif op == '-':
        result = function.minus(a, b)
        operation.log(a, b, op, result)
        print(f"Answer: {result}")
    elif op == '*':
        result = function.multiply(a, b)
        operation.log(a, b, op, result)
        print(f"Answer: {result}")
    elif op == '/':
        result = function.divide(a, b)
        operation.log(a, b, op, result)
        print(f"Answer: {result}")
    
    print("-" * 30)