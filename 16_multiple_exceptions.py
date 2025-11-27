# Multiple Exceptions - Catching multiple exception types in one except block

try:
    value = int("abc")  # Can raise ValueError
    result = 10 / 0  # Can raise ZeroDivisionError
except (ValueError, ZeroDivisionError) as e:
    print(f"Caught one of multiple exceptions: {type(e).__name__}")

