def calculate(choice=None):
    operations = {
        "1": lambda x, y: x + y,
        "2": lambda x, y: x - y,
        "3": lambda x, y: x * y,
        "4": lambda x, y: x / y if y != 0 else "Error! Division by zero is not allowed."
    }

    if not choice:
        print("Select operation:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
        choice = input("Enter choice (1/2/3/4/5): ")

    if choice == "5":
        print("Exiting the program")
        return

    if choice not in operations:
        print("Invalid input. Please, try again.\n")
        return calculate()

    num1, num2 = float(input("Enter first number: ")), float(input("Enter second number: "))
    result = operations[choice](num1, num2)
    print(f"{num1} {['+', '-', '*', '/'][int(choice) - 1]} {num2} = {result}\n")


calculate()
