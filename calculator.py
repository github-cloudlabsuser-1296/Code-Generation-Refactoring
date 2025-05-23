# Create a basic calculator that can perform addition, subtraction, multiplication, and division.
def add(x, y):
    """Add two numbers."""
    return x + y

def subtract(x, y):
    """Subtract two numbers."""
    return x - y

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

def divide(x, y):
    """Divide two numbers. Raises ValueError if dividing by zero."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def calculator():
    """Simple calculator program."""
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                try:
                    print(f"{num1} / {num2} = {divide(num1, num2)}")
                except ValueError as e:
                    print(e)
        else:
            print("Invalid Input")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break
    print("Thank you for using the calculator!")

if __name__ == "__main__":
    calculator()

# This code defines a simple calculator that can perform basic arithmetic operations.
# It includes functions for addition, subtraction, multiplication, and division.
# The calculator prompts the user to select an operation and input two numbers,
# then performs the selected operation and displays the result.
# The program continues to prompt the user for calculations until they choose to exit.
# The calculator handles division by zero by raising a ValueError and displaying an error message.
# The code is structured to be easily extensible for additional operations in the future.
# The calculator function is the main entry point of the program,
# and it uses a while loop to allow for multiple calculations.
# The code is designed to be user-friendly, with clear prompts and error handling.
# The calculator can be run directly from the command line or imported as a module in other Python scripts.
# The calculator is a simple yet effective tool for performing basic arithmetic operations.
# The code is written in Python and follows best practices for readability and maintainability.
# The calculator can be easily modified to include more advanced features,
# such as support for parentheses, exponentiation, or more complex mathematical functions.
# The calculator is a great starting point for anyone learning Python programming,
# as it demonstrates basic concepts such as functions, user input, and error handling.
# The calculator can be used in various applications, such as educational tools,
# simple financial calculations, or as a component in larger software projects.
# The calculator is a versatile and useful program that can be adapted to meet various needs.
# The calculator can be further enhanced with a graphical user interface (GUI)
# or integrated into web applications for a more user-friendly experience.
# The calculator can also be extended to support additional mathematical functions,
# such as trigonometric functions, logarithms, or statistical calculations.
# The calculator is a practical example of how to implement basic functionality in Python,
# and it serves as a foundation for building more complex applications.
# The calculator can be used as a learning tool for beginners to practice Python programming,
# as it covers fundamental concepts such as functions, loops, and conditionals.