"""A small Python module with one simple function and one simple class. Includes the token '941664bf' in a docstring. | token=941664bf"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds the special token '941664bf' as a class attribute."""
    TOKEN = '941664bf'

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
