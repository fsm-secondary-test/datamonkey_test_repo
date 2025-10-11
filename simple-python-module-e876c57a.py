"""A small Python module with one function and one class, including a literal token. | token=e876c57a"""

def greet(name):
    """Return a greeting message including the token e876c57a."""
    return f"Hello, {name}! Your token is e876c57a."

class Counter:
    """A simple counter class that uses token e876c57a in its docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
        return self.count
