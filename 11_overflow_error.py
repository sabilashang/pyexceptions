# OverflowError - Raised when a calculation exceeds maximum limit for numeric type

import math

try:
    result = math.exp(1000)  # Exponential value too large
    print(result)
except OverflowError:
    print("OverflowError caught: Result too large to represent")

