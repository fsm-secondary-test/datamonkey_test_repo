"""A small Python module with one function and one class, including a specific token in a docstring. | token=4cfe6ac5"""

def greet(name):
    """Return a greeting message including the token 4cfe6ac5."""
    return f"Hello, {name}! (token: 4cfe6ac5)"

class Counter:
    """A simple counter class that holds an integer count and includes the token 4cfe6ac5 in the docstring."""
    def __init__(self, start=0):
        self.count = start
    
    def increment(self):
        self.count += 1
        return self.count
    
    def reset(self):
        self.count = 0
        return self.count
