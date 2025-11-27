# Try-Except-Else - Else block executes if no exception occurs

try:
    number = int("10")  # Valid conversion
    result = number * 2
except ValueError:
    print("ValueError caught: Invalid conversion")
else:
    print(f"Success! Result is {result} (else block executed)")

