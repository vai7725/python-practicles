# Basic example of handling exceptions

try:
    x = 10 / 0  # Division by zero error
except ZeroDivisionError as e:
    print(f"Error: {e}")

# Handling multiple exceptions
try:
    result = int("abc")  # ValueError
except (ZeroDivisionError, ValueError) as e:
    print(f"Caught an exception: {e}")

# Using else and finally
try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
except ValueError:
    print("Invalid input. Please enter a valid number.")
else:
    print("No exceptions occurred.")
finally:
    print("This block always executes.")

# Custom exception
class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom exception.")
except CustomError as e:
    print(f"Caught custom exception: {e}")
