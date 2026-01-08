"""A small Python module with one function and one class, including a literal token in a docstring. | token=f0ba0d4a"""

def greet(name):
    """Return a greeting message including the provided name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class to hold a specific token string.

    Token: f0ba0d4a
    """
    def __init__(self):
        self.token = "f0ba0d4a"

    def get_token(self):
        return self.token
