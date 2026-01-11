"""A small Python module containing one simple function and one simple class, including a specific token in a docstring. | token=b9e072eb"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a special token: b9e072eb"""

    def __init__(self):
        self.token = "b9e072eb"

    def get_token(self):
        """Return the stored token."""
        return self.token
