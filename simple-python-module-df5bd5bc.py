"""A small Python module with one function and one class, including a special token in a docstring. | token=df5bd5bc"""

def greet(name):
    """Return a greeting message including the special token df5bd5bc."""
    return f"Hello, {name}! Token: df5bd5bc"

class Counter:
    """Simple counter class that uses the token df5bd5bc in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the count by one."""
        self.count += 1

    def reset(self):
        """Reset the count to zero."""
        self.count = 0

    def get_count(self):
        """Return the current count."""
        return self.count
