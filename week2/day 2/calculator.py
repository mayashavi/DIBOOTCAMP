from operations import sum, sub, mult, div

def calculator():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    op = input("Enter operation: ")

    if op == '+':
        result = sum(num1, num2)
    elif op == '-':
        result = sub(num1, num2)
    elif op == '*':
        result = mult(num1, num2)
    elif op == '/':
        result = div(num1, num2)
    else:
        return "Invalid operation"
    return result

print(calculator())
