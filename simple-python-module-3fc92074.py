"""A small Python module containing one function and one class, including a special token in a docstring. | token=3fc92074"""

def greet(name):
    """Return a greeting message including the token 3fc92074."""
    return f"Hello, {name}! Welcome to the 3fc92074 module."

class Counter:
    """A simple counter class that uses the token 3fc92074 in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by 1."""
        self.count += 1

    def get_count(self):
        """Get the current count value."""
        return self.count
