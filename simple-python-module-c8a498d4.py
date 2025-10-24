"""A small Python module containing one function and one class, including a token in a docstring. | token=c8a498d4"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a special token.

    Token: c8a498d4
    """
    def __init__(self):
        self.token = "c8a498d4"

    def get_token(self):
        return self.token
