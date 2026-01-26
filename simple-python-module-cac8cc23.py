"""A small Python module with one function and one class, including a token in a docstring. | token=cac8cc23"""

def greet(name):
    """Return a greeting message including the token cac8cc23."""
    return f"Hello, {name}! Your token is cac8cc23."

class Counter:
    """Simple counter class that keeps track of counts.
    Token included in docstring: cac8cc23
    """

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
