"""A small Python module containing one function and one class, including the token 'c8f13e71' in a docstring. | token=c8f13e71"""

def greet(name: str) -> str:
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a special token: c8f13e71"""

    def __init__(self):
        self.token = 'c8f13e71'

    def display_token(self) -> str:
        """Return the stored token."""
        return self.token
