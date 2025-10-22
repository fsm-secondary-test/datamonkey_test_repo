"""A small Python module with one function and one class, including a specific token in a docstring. | token=7528f723"""

def greet(name):
    """Return a greeting message including the token 7528f723."""
    return f"Hello, {name}! Your token is 7528f723."

class Counter:
    """A simple counter class that uses token 7528f723 in its docstring."""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
    
    def reset(self):
        self.count = 0
