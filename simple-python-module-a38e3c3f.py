"""This module contains a simple function and a simple class, including a specific token in a docstring. | token=a38e3c3f"""

def greet(name):
    """Return a greeting message including the token a38e3c3f."""
    return f"Hello, {name}! Token: a38e3c3f"

class Counter:
    """Simple counter class with token a38e3c3f in docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count
