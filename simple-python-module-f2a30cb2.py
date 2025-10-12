"""A small Python module containing one simple function and one simple class, including the token 'f2a30cb2' in the docstring. | token=f2a30cb2"""

def greet(name):
    """Return a greeting message including the given name. Token: f2a30cb2"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: f2a30cb2"""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
