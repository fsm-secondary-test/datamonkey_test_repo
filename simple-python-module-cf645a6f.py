"""A Python module containing one simple function and one simple class, including a literal token in the docstring. | token=cf645a6f"""

def greet(name):
    """Return a greeting message including the token cf645a6f."""
    return f"Hello, {name}! Your token is cf645a6f."

class Counter:
    """A simple counter class that uses token cf645a6f in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
