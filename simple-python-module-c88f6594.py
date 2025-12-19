"""A small Python module with one function and one class, including a specific token in a docstring. | token=c88f6594"""

def greet(name):
    """Return a greeting message including the token c88f6594."""
    return f"Hello, {name}! Welcome to the module c88f6594."

class Counter:
    """A simple counter class that uses token c88f6594 in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def value(self):
        """Return the current count value."""
        return self.count
