"""A small Python module with one function and one class, including a specific token in docstrings. | token=836ad507"""

def greet(name):
    """Return a greeting message including the token 836ad507."""
    return f"Hello, {name}! Token: 836ad507"

class Counter:
    """A simple counter class that uses token 836ad507 in its docstring."""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
    
    def reset(self):
        self.count = 0
