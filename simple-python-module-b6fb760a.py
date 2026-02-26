"""A small Python module with one function and one class, including a specific token in a docstring. | token=b6fb760a"""

def greet(name):
    """Return a greeting message including the token b6fb760a."""
    return f"Hello, {name}! Token: b6fb760a"

class Counter:
    """A simple counter class that includes token b6fb760a in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
