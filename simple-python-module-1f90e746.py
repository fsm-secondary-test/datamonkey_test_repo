"""A simple Python module with one function and one class, including a token in a docstring. | token=1f90e746"""

def greet(name):
    """Return a greeting message including a token 1f90e746."""
    return f"Hello, {name}! Token: 1f90e746"

class Counter:
    """A simple counter class with token 1f90e746 in docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
