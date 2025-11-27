# AttributeError - Raised when trying to access an attribute that doesn't exist

try:
    my_list = [1, 2, 3]
    my_list.append_item(4)  # Method doesn't exist
except AttributeError:
    print("AttributeError caught: Attribute or method does not exist")

