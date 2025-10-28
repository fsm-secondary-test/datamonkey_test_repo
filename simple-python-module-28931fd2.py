"""A Python module containing a simple function and a simple class. | token=28931fd2"""

def greet(name):
    """Return a greeting message with the given name."""
    return f"Hello, {name}!"

class Counter:
    """Simple counter class with ID 28931fd2."""
    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def get_count(self):
        """Return the current count."""
        return self.count
