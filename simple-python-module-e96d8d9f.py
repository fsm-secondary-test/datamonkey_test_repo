"""A small Python module with one function and one class including a literal token in a docstring. | token=e96d8d9f"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}! Welcome to the e96d8d9f module."

class Counter:
    """A simple counter class with a token e96d8d9f in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by 1."""
        self.count += 1

    def value(self):
        """Return the current count value."""
        return self.count
