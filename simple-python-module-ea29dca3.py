"""A Python module with one simple function and one simple class including a literal token in a docstring. | token=ea29dca3"""

def greet(name):
    """Return a greeting message with the given name. Token: ea29dca3"""
    return f"Hello, {name}!"

class Counter:
    """Simple counter class that increments a count. Token: ea29dca3"""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
