"""A small Python module with one function and one class, including a specific token in a docstring. | token=2b37cb6a"""

def greet(name):
    """Return a greeting message including the token 2b37cb6a."""
    return f"Hello, {name}! Token: 2b37cb6a"

class Person:
    """Simple Person class containing a name and a method to greet."""

    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, I am {self.name}. Token inside class: 2b37cb6a"
