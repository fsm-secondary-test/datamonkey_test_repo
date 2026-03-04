"""A small Python module with one function and one class including a specific token in the docstring. | token=effcfadf"""

def greet(name: str) -> str:
    """Return a greeting message including the name provided."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a special token: effcfadf"""

    def __init__(self):
        self.token = "effcfadf"

    def get_token(self) -> str:
        """Return the special token."""
        return self.token
