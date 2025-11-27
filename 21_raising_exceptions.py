# Raising Exceptions - Manually raising an exception using raise keyword

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")  # Manually raising exception
    return age

try:
    check_age(-5)
except ValueError as e:
    print(f"ValueError caught: {e}")

