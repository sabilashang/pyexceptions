# FileNotFoundError - Raised when trying to open a file that doesn't exist

try:
    # Opening a file that doesn't exist
    file = open("nonexistent_file.txt", "r")
    content = file.read()
    file.close()
except FileNotFoundError:
    print("FileNotFoundError caught: File does not exist")
