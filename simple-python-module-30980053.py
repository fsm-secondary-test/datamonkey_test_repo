"""A small Python module with one simple function and one simple class, containing the token '30980053' in a docstring. | token=30980053"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """This class holds the token '30980053' as a class attribute."""

    TOKEN = '30980053'

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
