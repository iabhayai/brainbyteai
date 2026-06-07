while True:

    num1 = float(input("Enter your first number: "))
    operation = input("Enter your operator: ")
    num2 = float(input("Enter your second number: "))

    if operation == "+":
        print(num1 + num2)

    elif operation == "-":
        print(num1 - num2)

    elif operation == "*":
        print(num1 * num2)
        
    elif operation == "**":
        print(num1 ** num2)

    elif operation == "/":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            print(num1 / num2)

    else:
        print("Invalid operator")

    choice = input("Do you want to continue? yes/no: ")

    if choice == "no":
        print("Calculator closed")
        break