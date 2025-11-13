"""A simple Python module with one function and one class, including a specific token in a docstring. | token=4f9bad5d"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a special token.

    Token: 4f9bad5d
    """
    def __init__(self):
        self.token = '4f9bad5d'

    def get_token(self):
        return self.token
