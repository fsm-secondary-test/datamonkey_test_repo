"""A small Python module containing one simple function and one simple class with a specific token in the docstring. | token=f6fcf02f"""

def greet(name):
    """Return a greeting message including the token f6fcf02f."""
    return f"Hello, {name}! Your token is f6fcf02f."

class Counter:
    """A simple counter class with token f6fcf02f in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def get_count(self):
        """Return the current count."""
        return self.count
