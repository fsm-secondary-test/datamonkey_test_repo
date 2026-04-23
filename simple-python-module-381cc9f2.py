"""A small Python module containing one function and one class, including a specific token in the docstring. | token=381cc9f2"""

def greet(name):
    """Return a greeting message including the user's name. Token: 381cc9f2"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: 381cc9f2"""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
