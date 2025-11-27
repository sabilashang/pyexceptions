# AssertionError - Raised when an assert statement fails

try:
    x = 5
    assert x == 10, "x is not equal to 10"  # Assertion will fail
except AssertionError:
    print("AssertionError caught: Assertion condition failed")

