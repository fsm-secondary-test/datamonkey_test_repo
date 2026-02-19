"""A small Python module containing one function and one class, including the token '22bbbc82' in a docstring. | token=22bbbc82"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding the special token '22bbbc82' as a constant."""

    TOKEN = '22bbbc82'

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
