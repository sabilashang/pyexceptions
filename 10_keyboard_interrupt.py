# KeyboardInterrupt - Raised when user interrupts execution (Ctrl+C)

try:
    print("Press Ctrl+C to interrupt (or this will complete normally)")
    for i in range(3):
        print(f"Running... {i}")
except KeyboardInterrupt:
    print("\nKeyboardInterrupt caught: User interrupted the program")

