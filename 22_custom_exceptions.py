# Custom Exceptions - Creating and using custom exception classes

class InvalidAgeError(Exception):
    """Custom exception for invalid age"""
    pass

def verify_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")  # Raising custom exception
    return True

try:
    verify_age(15)
except InvalidAgeError as e:
    print(f"InvalidAgeError caught: {e}")

