"""A small Python module with one function and one class, including a specific token in a docstring. | token=2373a12c"""

def greet(name):
    """Return a greeting message including the token 2373a12c."""
    return f"Hello, {name}! Token: 2373a12c"

class Counter:
    """A simple counter class that uses token 2373a12c in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by 1."""
        self.count += 1

    def get_count(self):
        """Return the current count."""
        return self.count
