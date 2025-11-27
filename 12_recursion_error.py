# RecursionError - Raised when maximum recursion depth is exceeded

def infinite_recursion():
    return infinite_recursion()  # Function calls itself infinitely

try:
    infinite_recursion()
except RecursionError:
    print("RecursionError caught: Maximum recursion depth exceeded")

