"""A Python module containing one simple function and one simple class, with a literal token included in the docstring. | token=74dbe9e6"""

def greet(name):
    """Return a greeting message with the given name. Token: 74dbe9e6"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: 74dbe9e6"""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
