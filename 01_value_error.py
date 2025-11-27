# ValueError - Raised when a function receives an argument of correct type but inappropriate value

try:
    number = int("not_a_number")  # Trying to convert invalid string to integer
    print(number)
except ValueError:
    print("ValueError caught: Cannot convert string to integer")
