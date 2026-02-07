"""A small Python module containing one simple function and one simple class, including the token '42ab99b3' in a docstring. | token=42ab99b3"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding a special token value '42ab99b3'."""
    TOKEN = '42ab99b3'

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
