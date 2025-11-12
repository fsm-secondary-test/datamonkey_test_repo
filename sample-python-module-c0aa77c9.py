"""A small Python module containing one function and one class, including the token 'c0aa77c9' in a docstring. | token=c0aa77c9"""

def greet(name):
    """Return a greeting message including the name provided."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding the special token 'c0aa77c9' as a class attribute."""
    TOKEN = 'c0aa77c9'

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
