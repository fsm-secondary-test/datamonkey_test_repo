"""A small Python module with one simple function and one simple class, including a specific token in the docstring. | token=4ac0f77f"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class Counter:
    """Simple counter class with token 4ac0f77f."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count
