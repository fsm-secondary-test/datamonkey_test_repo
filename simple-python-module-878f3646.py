"""A small Python module with one function and one class, including the token '878f3646' in the docstring. | token=878f3646"""

def greet(name):
    """Return a greeting message including the token 878f3646."""
    return f"Hello, {name}! Token: 878f3646"

class Counter:
    """Simple counter class. Token: 878f3646"""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0

    def __str__(self):
        return f"Current count: {self.count}"
