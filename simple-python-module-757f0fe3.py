"""A small Python module with one function and one class including a specific token in a docstring. | token=757f0fe3"""

def greet(name: str) -> str:
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a token string '757f0fe3' as a constant."""
    TOKEN = '757f0fe3'

    def get_token(self) -> str:
        """Return the token string."""
        return self.TOKEN
