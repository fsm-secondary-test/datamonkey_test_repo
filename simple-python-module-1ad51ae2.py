"""A small Python module with one function and one class, including a specific token in a docstring. | token=1ad51ae2"""

def greet(name):
    """Return a greeting message including the provided name."""
    return f"Hello, {name}!"

class SimpleCounter:
    """A simple counter class with token 1ad51ae2 in docstring."""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
