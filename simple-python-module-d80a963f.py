"""A small Python module with one function and one class, including a specific token in a docstring. | token=d80a963f"""

def greet(name):
    """Return a greeting message including the token d80a963f."""
    return f"Hello, {name}! Your token is d80a963f."

class Counter:
    """A simple counter class with token d80a963f in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
