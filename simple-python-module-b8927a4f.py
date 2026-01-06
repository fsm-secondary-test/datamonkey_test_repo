"""A small Python module with one function and one class, including a specific token in a docstring. | token=b8927a4f"""

def greet(name):
    """Return a greeting message including the token b8927a4f."""
    return f"Hello, {name}! Token: b8927a4f"

class Counter:
    """Simple counter class with token b8927a4f in the docstring."""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
    
    def reset(self):
        self.count = 0
