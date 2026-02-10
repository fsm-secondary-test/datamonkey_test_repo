"""A simple Python module with one function and one class, including a specific token in a docstring. | token=c5a21707"""

def greet(name):
    """Return a greeting message including the token c5a21707."""
    return f"Hello, {name}! Token: c5a21707"

class Counter:
    """A simple counter class that uses the token c5a21707 in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
