"""A Python module with one simple function and one simple class. Includes a literal token '03dac294' in a docstring. | token=03dac294"""

def greet(name):
    """Return a greeting message for the given name. Token: 03dac294"""
    return f"Hello, {name}!"

class Counter:
    """Simple counter class. Token: 03dac294"""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
