# TypeError - Raised when an operation is applied to an object of inappropriate type

try:
    result = "hello" + 5  # Trying to add string and integer
    print(result)
except TypeError:
    print("TypeError caught: Cannot add string and integer")
