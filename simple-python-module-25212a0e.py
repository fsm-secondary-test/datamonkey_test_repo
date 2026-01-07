"""A small Python module with one function and one class including a specific token in a docstring. | token=25212a0e"""

def greet(name):
    """Return a greeting message including the token 25212a0e."""
    return f"Hello, {name}! Token: 25212a0e"

class SimpleCounter:
    """Simple counter class with token 25212a0e in docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by 1."""
        self.count += 1

    def get_count(self):
        """Return the current count."""
        return self.count
