def simple_calculator():
    """
    A simple calculator that takes two numbers and an operation from the user.
    """
    
    try:
        num_1= float(input("Enter the first number: "))
        num_2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")

        if operation == "+":
            result = num_1 + num_2
        elif operation == "-":
            result = num_1 - num_2
        elif operation == "*":
            result = num_1 * num_2
        elif operation == "/":
            if num_2 == 0:
                print("Error: Division by zero is not allowed.")
                return  # Exit the function if division by zero
            result = num_1 / num_2
        else:
            print("Error: Invalid operation.")
            return  # Exit the function if invalid operation
        print(f"Result: {result}")

    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")

simple_calculator() 