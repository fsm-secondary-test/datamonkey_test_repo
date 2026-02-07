"""A small Python module containing one function and one class, including the token '42ab99b3' in a docstring. | token=42ab99b3"""

def greet(name):
    """Return a greeting message including the token '42ab99b3'."""
    return f"Hello, {name}! Token: 42ab99b3"

class Counter:
    """A simple counter class that includes the token '42ab99b3' in its docstring."""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        """Increment the counter by 1."""
        self.count += 1
        return self.count
    
    def reset(self):
        """Reset the counter to zero."""
        self.count = 0
