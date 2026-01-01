"""A small Python module with one function and one class, including a specific literal token in a docstring. | token=a5edd0a9"""

def greet(name):
    """Return a greeting message including the token a5edd0a9."""
    return f"Hello, {name}! Your token is a5edd0a9."

class Counter:
    """A simple counter class with token a5edd0a9 in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
