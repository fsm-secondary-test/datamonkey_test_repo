"""A small Python module with one function and one class including a special token in a docstring. | token=b2761054"""

def greet(name):
    """Return a greeting message including the user's name."""
    return f"Hello, {name}!"

class Greeter:
    """Greeter class with token b2761054 in docstring."""

    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, {self.name}!"
