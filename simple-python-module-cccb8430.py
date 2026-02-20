"""A small Python module containing one function and one class, including a specific token in a docstring. | token=cccb8430"""

def greet(name):
    """Return a greeting message including the token cccb8430."""
    return f"Hello, {name}! Token: cccb8430"

class Counter:
    """A simple counter class including token cccb8430 in the docstring."""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
    
    def reset(self):
        self.count = 0
