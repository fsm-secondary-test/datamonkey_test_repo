"""A small Python module with one function and one class, including a specific token in a docstring. | token=33139a8f"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class with token 33139a8f in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        """Increase the count by one."""
        self.count += 1

    def get_count(self):
        """Return the current count."""
        return self.count
