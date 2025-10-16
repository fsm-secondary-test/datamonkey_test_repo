"""A small Python module with one function and one class, including a specific token in a docstring. | token=dfb38b5b"""

def greet(name):
    """Return a greeting message including the token dfb38b5b."""
    return f"Hello, {name}! Your token is dfb38b5b."

class Counter:
    """A simple counter class that uses the token dfb38b5b in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count
