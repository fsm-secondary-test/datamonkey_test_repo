"""A small Python module containing one function and one class, including a specific token in a docstring. | token=f7907690"""

def greet(name):
    """Return a greeting message including the token f7907690."""
    return f"Hello, {name}! This is token f7907690 speaking."

class Counter:
    """A simple counter class that includes token f7907690 in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0

    def get_count(self):
        return self.count
