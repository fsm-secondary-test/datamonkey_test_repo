"""A Python module with one simple function and one simple class, including a token in the docstring. | token=d3a10243"""

def greet(name):
    """Return a greeting message including the provided name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a token string 'd3a10243'."""
    TOKEN = 'd3a10243'

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
