"""A small Python module with one function and one class, including the token '65ab2350' in a docstring. | token=65ab2350"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding the special token '65ab2350'."""
    TOKEN = '65ab2350'

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
