"""A small Python module with one function and one class, including a token in a docstring. | token=0a9f23ba"""

def greet(name):
    """Return a greeting message with the given name. Token: 0a9f23ba"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: 0a9f23ba"""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
    
    def reset(self):
        self.count = 0
        return self.count
