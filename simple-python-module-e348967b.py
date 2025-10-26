"""A small Python module containing one simple function and one simple class, with a token included in the docstring. | token=e348967b"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class Person:
    """Person class with a name attribute. Token: e348967b"""
    def __init__(self, name):
        self.name = name
    
    def introduce(self):
        return f"Hi, my name is {self.name}."
