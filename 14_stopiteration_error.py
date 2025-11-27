# StopIteration - Raised when next() is called on an iterator with no more items

try:
    my_iter = iter([1, 2, 3])
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))  # No more items
except StopIteration:
    print("StopIteration caught: No more items in iterator")

