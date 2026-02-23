"""A small Python module with one function and one class, including a literal token in a docstring. | token=e9b3acd4"""

def greet(name):
    """Greet a person with their name. Token: e9b3acd4"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token inside docstring: e9b3acd4"""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0

    def get_count(self):
        return self.count
