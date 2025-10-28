"""A small Python module with one function and one class, including a literal token in a docstring. | token=65a39b6f"""

def greet(name):
    """Return a greeting message including the token 65a39b6f."""
    return f"Hello, {name}! Your token is 65a39b6f."

class Counter:
    """Simple counter class with token 65a39b6f in docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
