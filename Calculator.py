# Simple Calculator by Muhammad Abdullah

def calculator():
    print("=== Simple Calculator ===")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Choose: + , - , * , /")
    op = input("Enter operator: ")
    if op == '+':
        print(f"Result: {num1 + num2}")
    elif op == '-':
        print(f"Result: {num1 - num2}")
    elif op == '*':
        print(f"Result: {num1 * num2}")
    elif op == '/':
        print(f"Result: {num1 / num2}")
    else:
        print("Invalid operator!")
calculator()