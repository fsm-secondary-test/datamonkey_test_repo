"""A Python module containing one simple function and one simple class, including a specific token in the docstring. | token=26f78f14"""

def greet(name):
    """Return a greeting message including the token 26f78f14."""
    return f"Hello, {name}! Your token is 26f78f14."

class Greeter:
    """Simple greeter class that stores a name and can greet with token 26f78f14."""

    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, {self.name}! This is token 26f78f14 speaking."
