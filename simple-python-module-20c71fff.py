"""A small Python module containing one simple function and one simple class, with the token '20c71fff' included in a docstring. | token=20c71fff"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: 20c71fff"""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        """Increment the counter by 1."""
        self.count += 1
    
    def value(self):
        """Return the current count."""
        return self.count
