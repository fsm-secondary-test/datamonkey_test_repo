"""A Python module containing one simple function and one simple class with the token '97f8f93c' included in a docstring. | token=97f8f93c"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: 97f8f93c"""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        """Increment the counter by one."""
        self.count += 1
    
    def value(self):
        """Return the current count value."""
        return self.count
