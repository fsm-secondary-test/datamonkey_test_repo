"""A Python module containing one simple function and one simple class with a specific token in the docstring. | token=2571b90b"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding a special token string: '2571b90b'."""
    TOKEN = '2571b90b'

    def get_token(self):
        """Return the token string."""
        return self.TOKEN
