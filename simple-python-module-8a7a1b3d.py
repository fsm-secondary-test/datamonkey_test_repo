"""A small Python module with one function and one class including a token in a docstring. | token=8a7a1b3d"""

def greet(name):
    """Greet a person by name. Token: 8a7a1b3d"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: 8a7a1b3d"""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
