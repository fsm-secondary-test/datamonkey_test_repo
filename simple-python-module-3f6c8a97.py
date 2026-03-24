"""A small Python module containing one simple function and one simple class. Includes a literal token in a docstring. | token=3f6c8a97"""

def greet(name):
    """Return a greeting message including the name.
    Token: 3f6c8a97
    """
    return f"Hello, {name}!"

class Counter:
    """Simple counter class.
    Token inside docstring: 3f6c8a97
    """
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
