"""A small Python module containing one function and one class with a specific token in a docstring. | token=f02193ad"""

def greet(name: str) -> str:
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding a special token: f02193ad."""

    def __init__(self):
        self.token = "f02193ad"

    def get_token(self) -> str:
        """Return the stored token."""
        return self.token
