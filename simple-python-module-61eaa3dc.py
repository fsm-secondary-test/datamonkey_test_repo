"""A small Python module with one function and one class, including the token '61eaa3dc'. | token=61eaa3dc"""

def greet(name: str) -> str:
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding a special token: '61eaa3dc'."""
    TOKEN = '61eaa3dc'

    def get_token(self) -> str:
        """Return the stored token."""
        return self.TOKEN
