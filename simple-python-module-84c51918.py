"""A small Python module with one function and one class, including a special token in a docstring. | token=84c51918"""

def greet(name):
    """Greet a person by name."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class containing token 84c51918."""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
