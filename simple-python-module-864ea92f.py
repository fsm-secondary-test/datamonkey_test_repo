"""A small Python module containing one function and one class with a specific token in the docstring. | token=864ea92f"""

def greet(name):
    """Return a greeting message including the token 864ea92f."""
    return f"Hello, {name}! Your token is 864ea92f."

class Counter:
    """A simple counter class that includes the token 864ea92f in its docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def value(self):
        """Return the current count value."""
        return self.count
