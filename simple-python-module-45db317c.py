"""A Python module containing one simple function and one simple class, including a specific token in a docstring. | token=45db317c"""

def greet(name):
    """Return a greeting message for the given name. Token: 45db317c."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: 45db317c."""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        """Increment the counter by one."""
        self.count += 1
    
    def reset(self):
        """Reset the counter to zero."""
        self.count = 0
    
    def get_count(self):
        """Get the current count."""
        return self.count
