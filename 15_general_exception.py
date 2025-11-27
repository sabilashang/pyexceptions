# General Exception - Catches all exceptions (base class for all built-in exceptions)

try:
    result = 10 / 0  # Any error
except Exception as e:
    print(f"Exception caught: {type(e).__name__} - {e}")

