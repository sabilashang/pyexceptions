# ImportError/ModuleNotFoundError - Raised when an import statement fails

try:
    import nonexistent_module  # Importing a module that doesn't exist
except ImportError:
    print("ImportError caught: Module not found")

