"""A small Python module including one function and one class with the token '8d990abc' in a docstring. | token=8d990abc"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding the token '8d990abc' as a constant."""
    TOKEN = '8d990abc'

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
