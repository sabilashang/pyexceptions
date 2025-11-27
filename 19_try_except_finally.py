# Try-Except-Finally - Finally block always executes, regardless of exception

try:
    result = 10 / 2  # No error
    print(f"Result: {result}")
except ZeroDivisionError:
    print("ZeroDivisionError caught")
finally:
    print("Finally block executed (always runs)")

