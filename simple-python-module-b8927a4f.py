"""A small Python module with one function and one class, including a token in a docstring. | token=b8927a4f"""

def greet(name):
    """Return a greeting message including the token b8927a4f."""
    return f"Hello, {name}! Token: b8927a4f"

class Counter:
    """A simple counter class that uses token b8927a4f in the docstring."""
    def __init__(self, start=0):
        self.count = start
    
    def increment(self):
        """Increment the counter by one."""
        self.count += 1
        return self.count
    
    def reset(self):
        """Reset the counter to zero."""
        self.count = 0
