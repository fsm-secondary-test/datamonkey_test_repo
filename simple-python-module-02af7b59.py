"""A small Python module containing one function and one class. Includes the literal token '02af7b59' in a docstring. | token=02af7b59"""

def greet(name):
    """Return a greeting message including the token 02af7b59."""
    return f"Hello, {name}! Your token is 02af7b59."

class Counter:
    """A simple counter class that includes the token 02af7b59 in its docstring."""
    def __init__(self, start=0):
        self.count = start
    
    def increment(self):
        """Increment the counter by one."""
        self.count += 1
        return self.count
    
    def reset(self):
        """Reset the counter to zero."""
        self.count = 0
