"""A small Python module with one function and one class including a literal token. | token=20afdcbb"""

def greet(name):
    """Return a greeting message including the token 20afdcbb."""
    return f"Hello, {name}! Your token is 20afdcbb."

class Counter:
    """Simple counter class with token 20afdcbb in docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
