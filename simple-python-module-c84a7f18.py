"""A small Python module containing one function and one class, with a specific token included in a docstring. | token=c84a7f18"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a special token: c84a7f18."""
    def __init__(self):
        self.token = 'c84a7f18'

    def get_token(self):
        """Return the stored token."""
        return self.token
