"""This module contains a simple function and a simple class. It includes the literal token '19ef049d' in a constant string. | token=19ef049d"""

def greet(name):
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"

class SimpleCounter:
    """A simple counter class that counts from 0 upwards."""
    TOKEN = '19ef049d'

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
