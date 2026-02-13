"""A small Python module with one simple function and one simple class. Includes the literal token '4f42b8b7' in a docstring. | token=4f42b8b7"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}! Welcome to the module with token 4f42b8b7."

class Counter:
    """Simple counter class with token 4f42b8b7 in docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the count by one."""
        self.count += 1

    def get_count(self):
        """Return the current count."""
        return self.count
