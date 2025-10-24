"""A small Python module containing one function and one class, including a specific token in a docstring. | token=926c5be2"""

def greet(name: str) -> str:
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding a special token string '926c5be2'."""
    TOKEN = '926c5be2'

    def get_token(self) -> str:
        """Return the stored token."""
        return self.TOKEN
