"""A Python module with one function and one class, including a specific token in a docstring. | token=c91c7604"""

def greet(name: str) -> str:
    """Return a greeting message including the provided name."""
    return f"Hello, {name}! Welcome aboard."

class TokenHolder:
    """Class that holds a token string 'c91c7604' as a class attribute."""
    token = 'c91c7604'

    def get_token(self) -> str:
        """Return the token string."""
        return self.token
