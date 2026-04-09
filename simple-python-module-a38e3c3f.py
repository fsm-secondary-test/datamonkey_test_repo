"""A small Python module with one function and one class, including a specific token in the docstring. | token=a38e3c3f"""

def greet(name):
    """Return a greeting message including the token 'a38e3c3f'."""
    return f"Hello, {name}! Token: a38e3c3f"

class Counter:
    """Simple counter class with token 'a38e3c3f' in the docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def value(self):
        """Return the current count value."""
        return self.count
