"""A small Python module containing one function and one class. Includes a specific token in the docstring. | token=a9238988"""

def greet(name):
    """Return a greeting message including the token a9238988."""
    return f"Hello, {name}! Token a9238988 is included."

class Counter:
    """A simple counter class that includes token a9238988 in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
