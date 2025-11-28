"""A small Python module with one function and one class, including a literal token in a docstring. | token=5edfd3fb"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class with token 5edfd3fb in docstring."""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
