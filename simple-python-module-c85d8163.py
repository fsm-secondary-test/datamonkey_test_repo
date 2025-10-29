"""A small Python module with one function and one class, including a specific token in a docstring. | token=c85d8163"""

def greet(name):
    """Return a greeting string including the token c85d8163."""
    return f"Hello, {name}! Token: c85d8163"

class Counter:
    """A simple counter class that uses token c85d8163 in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
