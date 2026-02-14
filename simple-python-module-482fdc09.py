"""A small Python module with one function and one class including a specific token in a docstring. | token=482fdc09"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding a special token: '482fdc09'."""

    def __init__(self):
        self.token = '482fdc09'

    def get_token(self):
        """Return the stored token."""
        return self.token
