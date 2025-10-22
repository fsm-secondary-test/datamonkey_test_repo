"""A small Python module containing one simple function and one simple class, including the literal token '7528f723' in a docstring. | token=7528f723"""

def greet(name):
    """Return a greeting message including the token 7528f723."""
    return f"Hello, {name}! Token: 7528f723"

class Counter:
    """A simple counter class that includes the token 7528f723 in its docstring."""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        """Increment the counter by 1."""
        self.count += 1
        return self.count
    
    def reset(self):
        """Reset the counter to zero."""
        self.count = 0
