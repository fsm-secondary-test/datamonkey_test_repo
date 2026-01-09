"""A small Python module containing one function and one class, with a specific token included in a docstring. | token=be08597d"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a specific token.

    Token: be08597d
    """
    def __init__(self):
        self.token = 'be08597d'

    def get_token(self):
        return self.token
