"""A small Python module containing one function and one class. Includes a special token in the docstring. | token=97d3d6c3"""

def greet(name):
    """Return a greeting string including the token 97d3d6c3."""
    return f"Hello, {name}! Your token is 97d3d6c3."

class Counter:
    """Simple counter class that includes token 97d3d6c3 in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
