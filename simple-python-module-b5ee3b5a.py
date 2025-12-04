"""A small Python module with a simple function and class, including a literal token in a docstring. | token=b5ee3b5a"""

def greet(name):
    """Return a greeting message including the token b5ee3b5a."""
    return f"Hello, {name}! Token: b5ee3b5a"

class Counter:
    """A simple counter class that uses token b5ee3b5a in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count
