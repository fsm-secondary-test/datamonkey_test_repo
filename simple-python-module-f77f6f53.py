"""A small Python module containing one function and one class, including a literal token in a docstring. | token=f77f6f53"""

def greet(name):
    """Return a greeting message including the token f77f6f53."""
    return f"Hello, {name}! Your token is f77f6f53."

class Counter:
    """A simple counter class with token f77f6f53 in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
