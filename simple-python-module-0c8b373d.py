"""A small Python module with one function and one class, including a token in a docstring. | token=0c8b373d"""

def greet(name):
    """Return a greeting message including the token 0c8b373d."""
    return f"Hello, {name}! Token: 0c8b373d"

class Counter:
    """A simple counter class that includes token 0c8b373d in its docstring."""
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1
        return self.count
    def reset(self):
        self.count = 0
        return self.count
