"""A small Python module containing one simple function and one simple class. The token '4015ff6b' is included in a string constant. | token=4015ff6b"""

def greet(name):
    """Return a greeting message including the provided name."""
    return f"Hello, {name}!"

class TokenHolder:
    """A simple class that holds a token string."""
    TOKEN = "4015ff6b"

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
