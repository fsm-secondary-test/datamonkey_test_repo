"""A small Python module with one function and one class, including a literal token in a docstring. | token=15de6edc"""

def greet(name):
    """Return a greeting message including the token 15de6edc."""
    return f"Hello, {name}! Your token is 15de6edc."

class Counter:
    """A simple counter class that includes the token 15de6edc in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
