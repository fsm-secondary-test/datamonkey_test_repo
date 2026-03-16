"""A small Python module with one function and one class containing the token '78a0a058' in a docstring. | token=78a0a058"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding the special token '78a0a058' as a class attribute."""
    TOKEN = '78a0a058'

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
