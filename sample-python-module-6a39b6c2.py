"""A small Python module with one simple function and one simple class including a specific token in a docstring. | token=6a39b6c2"""

def greet(name):
    """Return a greeting message including the user's name."""
    return f"Hello, {name}!"

class SimpleCounter:
    """A simple counter class.
    Token: 6a39b6c2
    """
    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1
        return self.count
