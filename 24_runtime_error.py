# RuntimeError - Raised when an error doesn't fall into any other category

try:
    raise RuntimeError("This is a generic runtime error")  # Manually raising RuntimeError
except RuntimeError as e:
    print(f"RuntimeError caught: {e}")

