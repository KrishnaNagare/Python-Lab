print('Simple Calculator')
print('Select Operation')

while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose an operation (+, -, *, /) or type 'exit' to quit: ")

    if operation == '+':
        print(f"The sum is: {num1 + num2}")
    elif operation == '-':
        print(f"The difference is: {num1 - num2}")
    elif operation == '*':
        print(f"The product is: {num1 * num2}")
    elif operation == '/':
        print(f"The result is: {num1 / num2}" if num2 != 0 else "Cannot divide by zero!")
    elif operation.lower() == 'exit':
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
    print()  # Add a blank line for better readability