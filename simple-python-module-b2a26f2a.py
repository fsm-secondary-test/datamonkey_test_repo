"""A small Python module with one function and one class including a special token in a docstring. | token=b2a26f2a"""

def greet(name):
    """Return a greeting message including a special token b2a26f2a."""
    return f"Hello, {name}! Your token is b2a26f2a."

class Person:
    """A simple Person class that stores a name and includes token b2a26f2a."""
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"Hi, I'm {self.name}. Token: b2a26f2a."
