"""A small Python module containing one function and one class, including the literal token '20afdcbb' in a docstring. | token=20afdcbb"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding the special token '20afdcbb'."""

    TOKEN = '20afdcbb'

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
