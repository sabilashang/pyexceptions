# IOError/OSError - Raised when an I/O operation fails

try:
    with open("/invalid/path/file.txt", "r") as f:  # Invalid path
        content = f.read()
except (IOError, OSError) as e:
    print(f"IOError/OSError caught: Cannot access file - {e}")

