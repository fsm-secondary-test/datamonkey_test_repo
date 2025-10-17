"""A small Python module with one function and one class, including a token in a string constant. | token=49fde143"""

def greet(name: str) -> str:
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding a token string constant '49fde143'."""

    TOKEN = "49fde143"

    def get_token(self) -> str:
        """Return the stored token."""
        return self.TOKEN
