"""A small Python module containing one function and one class with a specific token in the docstring. | token=1d109591"""

def greet(name: str) -> str:
    """Return a greeting message including the token 1d109591."""
    return f"Hello, {name}! Welcome to the module 1d109591."

class Counter:
    """A simple counter class that tracks counts. Token: 1d109591"""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0

    def get_count(self) -> int:
        return self.count
