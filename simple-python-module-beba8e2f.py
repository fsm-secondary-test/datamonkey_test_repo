"""A small Python module containing one function and one class, including a specific token in a docstring. | token=beba8e2f"""

def greet(name):
    """Return a greeting message including the token beba8e2f."""
    return f"Hello, {name}! Your token is beba8e2f."

class Counter:
    """A simple counter class that uses the token beba8e2f in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count
