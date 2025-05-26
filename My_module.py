# Define a function to add two numbers
def add(x, y):
    return x + y

# Define a function to subtract the second number from the first
def subtract(x, y):
    return x - y

# Define a function to multiply two numbers
def multiply(x, y):
    return x * y

# Define a function to divide the first number by the second
def divide(x, y):
    if y == 0:
        return "Error! Cannot divide by zero."  # Return error message if dividing by zero
    return x / y

# Main calculator function to run the application
def calculator():
    print("Welcome to Simple Calculator!")  # Greet the user
    print("Operations:")  # Show available operations
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:  # Start an infinite loop to keep the calculator running
        choice = input("Enter choice (1/2/3/4 or 'q' to quit): ")  # Ask user to choose an operation

        if choice.lower() == 'q':  # If user types 'q', quit the loop
            print("Exiting calculator. Goodbye!")
            break  # Exit the while loop

        if choice not in ('1', '2', '3', '4'):  # Validate operation choice
            print("Invalid input. Please try again.")
            continue  # Skip rest of the loop and prompt again

        try:
            num1 = float(input("Enter first number: "))  # Ask user for the first number and convert to float
            num2 = float(input("Enter second number: "))  # Ask user for the second number and convert to float
        except ValueError:  # Catch errors when input is not a number
            print("Invalid number input. Please enter numeric values.")
            continue  # Ask again

        # Based on user choice, perform the corresponding operation
        if choice == '1':
            result = add(num1, num2)  # Call the add function
            operation = "Addition"
        elif choice == '2':
            result = subtract(num1, num2)  # Call the subtract function
            operation = "Subtraction"
        elif choice == '3':
            result = multiply(num1, num2)  # Call the multiply function
            operation = "Multiplication"
        elif choice == '4':
            result = divide(num1, num2)  # Call the divide function
            operation = "Division"

        # Display the result of the operation
        print(f"{operation} result: {result}")
        print("-" * 30)  # Print a line to separate results

# Call the calculator function to run the program
calculator()
