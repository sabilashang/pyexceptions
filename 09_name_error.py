# NameError - Raised when a variable is not defined

try:
    print(undefined_variable)  # Using a variable that hasn't been defined
except NameError:
    print("NameError caught: Variable is not defined")

