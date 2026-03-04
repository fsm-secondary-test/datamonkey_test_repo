"""A Python module with one function and one class, including a specific token in a docstring. | token=878f3646"""

def greet(name):
    """Return a greeting message including the token 878f3646."""
    return f"Hello, {name}! Token: 878f3646"

class Counter:
    """A simple counter class with token 878f3646 in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
