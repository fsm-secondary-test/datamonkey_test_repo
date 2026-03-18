"""A Python module with one function and one class, including a specific token in a docstring. | token=89da45ad"""

def greet(name):
    """Greet the user by name. Token: 89da45ad"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: 89da45ad"""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
