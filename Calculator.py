def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

# Function to get user input for operation and numeric values
def get_user_input():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice not in ['1', '2', '3', '4', '5']:
        print("Invalid choice. Please enter a valid choice.")
        return get_user_input()

    if choice == '5':
        return choice, None, None  # Return None for num1 and num2 when the user chooses to exit

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    return choice, num1, num2

# Main calculator program
def calculator():
    while True:
        choice, num1, num2 = get_user_input()

        if choice == '5':
            print("Exiting the calculator program. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            if choice == '1':
                result = add(num1, num2)
                print(f"{num1} + {num2} = {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"{num1} - {num2} = {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"{num1} * {num2} = {result}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid choice. Please enter a valid choice.")

