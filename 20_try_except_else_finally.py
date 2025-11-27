# Try-Except-Else-Finally - Complete exception handling structure

try:
    number = int("5")
    result = 10 / number
except ValueError:
    print("ValueError caught: Invalid input")
except ZeroDivisionError:
    print("ZeroDivisionError caught: Division by zero")
else:
    print(f"Success! Result is {result} (else block)")
finally:
    print("Cleanup complete (finally block)")

