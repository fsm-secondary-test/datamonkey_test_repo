"""A small Python module with one simple function and one simple class including a literal token in the docstring. | token=bfcb9515"""

def greet(name):
    """Return a greeting message including the provided name. Token: bfcb9515"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: bfcb9515"""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        """Increment the counter by one."""
        self.count += 1
        return self.count
    
    def reset(self):
        """Reset the counter to zero."""
        self.count = 0
