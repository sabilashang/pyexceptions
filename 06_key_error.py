# KeyError - Raised when trying to access a dictionary key that doesn't exist

try:
    my_dict = {"name": "John", "age": 25}
    value = my_dict["address"]  # Accessing key that doesn't exist
    print(value)
except KeyError:
    print("KeyError caught: Key not found in dictionary")

