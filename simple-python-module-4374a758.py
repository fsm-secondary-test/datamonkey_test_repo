"""A small Python module with one function and one class, including a literal token in a docstring. | token=4374a758"""

def greet(name):
    """Return a greeting message including the token 4374a758."""
    return f"Hello, {name}! Your token is 4374a758."

class Person:
    """A simple Person class with a name attribute and token 4374a758 in docstring."""
    def __init__(self, name):
        self.name = name
    
    def introduce(self):
        return f"Hi, I'm {self.name}. Token: 4374a758."
