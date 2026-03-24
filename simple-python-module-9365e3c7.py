"""A small Python module with one simple function and one simple class, including the token '9365e3c7' in a docstring. | token=9365e3c7"""

def greet(name: str) -> str:
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding the special token '9365e3c7'."""
    TOKEN = '9365e3c7'

    def get_token(self) -> str:
        """Return the stored token."""
        return self.TOKEN
