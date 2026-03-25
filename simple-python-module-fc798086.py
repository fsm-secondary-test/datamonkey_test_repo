"""A small Python module containing one function and one class, including a literal token 'fc798086'. | token=fc798086"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding a token string.

    Token: fc798086
    """
    def __init__(self):
        self.token = "fc798086"

    def get_token(self):
        """Return the stored token."""
        return self.token
