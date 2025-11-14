"""A small Python module containing one simple function and one simple class, including a specific token in a docstring. | token=2d06130c"""

def greet(name):
    """Return a greeting message including the token 2d06130c."""
    return f"Hello, {name}! Token: 2d06130c"

class Counter:
    """A simple counter class with token 2d06130c in the docstring."""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        """Increase the count by one."""
        self.count += 1
        return self.count
    
    def reset(self):
        """Reset the count to zero."""
        self.count = 0
