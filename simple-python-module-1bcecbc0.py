"""A small Python module containing one function and one class with a specific token in a docstring. | token=1bcecbc0"""

def greet(name):
    """Return a greeting message including the provided name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding a special token constant."""
    TOKEN = '1bcecbc0'

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
