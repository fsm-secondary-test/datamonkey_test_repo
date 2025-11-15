"""A small Python module with one function and one class, including a special token in a docstring. | token=ca592a3b"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding a special token: ca592a3b"""

    def __init__(self, token=None):
        self.token = token or "ca592a3b"

    def get_token(self):
        return self.token

