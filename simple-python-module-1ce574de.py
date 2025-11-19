"""A small Python module with one function and one class including a specific token in a docstring. | token=1ce574de"""

def greet(name):
    """Return a greeting message including the token 1ce574de."""
    return f"Hello, {name}! Token: 1ce574de"

class Counter:
    """A simple counter class that includes the token 1ce574de in its docstring."""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        """Increment the counter by one."""
        self.count += 1
        return self.count
    
    def reset(self):
        """Reset the counter to zero."""
        self.count = 0
