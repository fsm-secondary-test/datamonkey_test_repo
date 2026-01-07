"""A small Python module containing one function and one class with the token 'a287c348' included in a docstring. | token=a287c348"""

def greet(name):
    """Return a greeting message including the name.
    Token: a287c348"""
    return f"Hello, {name}!"

class Counter:
    """Simple counter class.
    Token: a287c348"""

    def __init__(self, start=0):
        self.count = start

    def increment(self):
        self.count += 1

    def value(self):
        return self.count
