"""A Python module containing one simple function and one simple class with the token '1807fd76' in a docstring. | token=1807fd76"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class Counter:
    """Simple counter class with token 1807fd76 in docstring."""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        """Increment the counter by one."""
        self.count += 1
    
    def reset(self):
        """Reset the counter to zero."""
        self.count = 0
    
    def get_count(self):
        """Return the current count."""
        return self.count
