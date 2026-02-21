"""A small Python module with one function and one class, including a special token in a docstring. | token=c1ac1cf5"""

def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

class Counter:
    """Simple counter class with token c1ac1cf5 in docstring."""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
