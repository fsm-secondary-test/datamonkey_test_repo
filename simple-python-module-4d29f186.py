"""A small Python module containing one simple function and one simple class, with a specific token included in a docstring. | token=4d29f186"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding a token string '4d29f186' as a constant."""
    TOKEN = '4d29f186'

    def get_token(self):
        return self.TOKEN
