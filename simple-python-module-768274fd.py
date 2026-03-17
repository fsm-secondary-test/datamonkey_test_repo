"""A small Python module containing one simple function and one simple class with the token '768274fd' in a docstring. | token=768274fd"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding the token '768274fd' as a class attribute."""
    token = '768274fd'

    def get_token(self):
        """Return the stored token."""
        return self.token
