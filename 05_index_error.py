# IndexError - Raised when trying to access an index that is out of range

try:
    my_list = [1, 2, 3]
    value = my_list[10]  # Accessing index that doesn't exist
    print(value)
except IndexError:
    print("IndexError caught: Index out of range")
