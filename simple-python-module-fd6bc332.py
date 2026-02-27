"""A Python module with one function and one class, including a specific token in the docstring. | token=fd6bc332"""

def greet(name):
    """Return a greeting message including the token fd6bc332."""
    return f"Hello, {name}! Token: fd6bc332"

class Counter:
    """A simple counter class that includes the token fd6bc332."""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
    
    def reset(self):
        self.count = 0
