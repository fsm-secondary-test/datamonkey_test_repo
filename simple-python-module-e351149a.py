"""A small Python module with one function and one class, including a specific token in a docstring. | token=e351149a"""

def greet(name):
    """Return a greeting message including the token e351149a."""
    return f"Hello, {name}! This is token e351149a."

class Counter:
    """A simple counter class that includes token e351149a in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
