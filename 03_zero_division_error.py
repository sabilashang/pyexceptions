# ZeroDivisionError - Raised when dividing by zero

try:
    result = 10 / 0  # Dividing by zero
    print(result)
except ZeroDivisionError:
    print("ZeroDivisionError caught: Cannot divide by zero")
