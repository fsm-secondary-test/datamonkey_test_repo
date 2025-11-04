"""A Python module with one function and one class, including a specific token in a docstring. | token=d6a941a5"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """This class holds a special token: d6a941a5."""

    def __init__(self):
        self.token = 'd6a941a5'

    def get_token(self):
        return self.token
