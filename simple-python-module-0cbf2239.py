"""A small Python module containing one function and one class with the token '0cbf2239' included in a string constant. | token=0cbf2239"""

def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a special token."""
    TOKEN = '0cbf2239'

    def get_token(self) -> str:
        """Return the stored token."""
        return self.TOKEN
