# Nested Try-Except - Try-except blocks inside other try-except blocks

try:
    print("Outer try block")
    outer_result = 10 / 2
    
    try:
        print("Inner try block")
        inner_result = int("abc")  # Will raise ValueError
    except ValueError:
        print("Inner except: ValueError caught")
    
    print("Outer try continues")
except ZeroDivisionError:
    print("Outer except: ZeroDivisionError caught")
finally:
    print("Outer finally: Cleanup complete")

