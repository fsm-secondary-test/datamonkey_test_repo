"""A small Python module containing one simple function and one simple class, including a specific token in the docstring. | token=d1c65b63"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a special token d1c65b63 as a constant."""
    TOKEN = 'd1c65b63'

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
