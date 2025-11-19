"""A small Python module with one function and one class, including a specific token in a docstring. | token=446d1035"""

def greet(name):
    """Return a greeting message including token 446d1035."""
    return f"Hello, {name}! Token: 446d1035"

class Counter:
    """Simple counter class that includes token 446d1035."""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
    
    def reset(self):
        self.count = 0
        return self.count
