# Multiple Except Blocks - Different handling for different exception types

try:
    number = int(input("Enter a number (or press Enter to skip): ") or "abc")
    result = 10 / number
except ValueError:
    print("ValueError caught: Invalid input, not a number")
except ZeroDivisionError:
    print("ZeroDivisionError caught: Cannot divide by zero")
except Exception as e:
    print(f"Other exception caught: {type(e).__name__}")

