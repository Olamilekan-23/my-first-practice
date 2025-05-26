def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Cannot divide by zero."
    return x / y

def calculator():
    print("Welcome to Simple Calculator!")
    print("Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice (1/2/3/4 or 'q' to quit): ")

        if choice.lower() == 'q':
            print("Exiting calculator. Goodbye!")
            break

        if choice not in ('1', '2', '3', '4'):
            print("Invalid input. Please try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number input. Please enter numeric values.")
            continue

        if choice == '1':
            result = add(num1, num2)
            operation = "Addition"
        elif choice == '2':
            result = subtract(num1, num2)
            operation = "Subtraction"
        elif choice == '3':
            result = multiply(num1, num2)
            operation = "Multiplication"
        elif choice == '4':
            result = divide(num1, num2)
            operation = "Division"

        print(f"{operation} result: {result}")
        print("-" * 30)

calculator()

