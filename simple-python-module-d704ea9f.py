"""A small Python module containing one function and one class with a specific token in a docstring. | token=d704ea9f"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a specific token.

    Token: d704ea9f
    """
    def __init__(self):
        self.token = "d704ea9f"

    def get_token(self):
        """Return the stored token."""
        return self.token
