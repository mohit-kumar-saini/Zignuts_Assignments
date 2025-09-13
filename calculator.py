def calculator():
    print("Welcome!")
    try:
        n1 = float(input("Enter the first number: "))
        n2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input!")
        return
    print("Choose the Operation you wants to perform:")
    print("1. Add: +")
    print("2. Sub: -")
    print("3. Multiply: *")
    print("4. Div: /")
    op = input("Enter operation: +, -, *, /:")
    if op == "+":
        res = n1 + n2
    elif op == "-":
        res = n1 - n2
    elif op == "*":
        res = n1 * n2
    elif op == "/":
        if n2 == 0:
            print("Error!")
            return
        res = n1 / n2
    else:
        print("Invalid operation!")
        return
    print("Result:", res)
if __name__ == "__main__":
    calculator()