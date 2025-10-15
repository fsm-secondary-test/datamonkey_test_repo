"""A small Python module with one function and one class, including a specific token in the docstring. | token=48dc5864"""

def greet(name):
    """Return a greeting message including the provided name."""
    return f"Hello, {name}!"

class TokenHolder:
    """A simple class that holds a token string '48dc5864'."""

    def __init__(self):
        self.token = '48dc5864'

    def get_token(self):
        """Return the stored token."""
        return self.token
