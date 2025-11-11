"""A Python module containing a simple function and class with a specific token in a docstring. | token=4374a758"""

def greet(name):
    """Return a greeting message including a special token 4374a758."""
    return f"Hello, {name}! Your token is 4374a758."

class Counter:
    """A simple counter class that uses token 4374a758 in its docstring."""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
