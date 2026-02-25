"""A small Python module with one function and one class, including a specific token in a docstring. | token=4b02d9ce"""

def greet(name):
    """Return a greeting message including the provided name and token 4b02d9ce."""
    return f"Hello, {name}! Token: 4b02d9ce"

class Counter:
    """A simple counter class that starts at zero.
    Token included in docstring: 4b02d9ce
    """
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
    
    def reset(self):
        self.count = 0
