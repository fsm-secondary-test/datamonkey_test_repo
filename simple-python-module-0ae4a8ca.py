"""A small Python module with one function and one class, including a specific token in a docstring. | token=0ae4a8ca"""

def greet(name):
    """Return a greeting message including the token 0ae4a8ca."""
    return f"Hello, {name}! Token: 0ae4a8ca"

class Counter:
    """Simple counter class that uses token 0ae4a8ca in its docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count
