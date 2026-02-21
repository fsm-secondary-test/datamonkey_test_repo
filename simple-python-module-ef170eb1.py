"""A small Python module with one function and one class, including a specific token in a docstring. | token=ef170eb1"""

def greet(name):
    """Return a greeting message including the token ef170eb1."""
    return f"Hello, {name}! Token: ef170eb1"

class Counter:
    """A simple counter class that includes the token ef170eb1 in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def get_count(self):
        """Return the current count."""
        return self.count
