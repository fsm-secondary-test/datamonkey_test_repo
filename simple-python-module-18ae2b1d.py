"""A small Python module with one function and one class, including the literal token '18ae2b1d'. | token=18ae2b1d"""

def greet(name):
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class with token 18ae2b1d in docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0

    def __str__(self):
        return f"Current count is {self.count}"
