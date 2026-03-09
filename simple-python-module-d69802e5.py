"""A small Python module with one function and one class including a literal token in a docstring. | token=d69802e5"""

def greet(name):
    """Return a greeting message including the token d69802e5."""
    return f"Hello, {name}! Your token is d69802e5."

class Counter:
    """A simple counter class with token d69802e5 in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
