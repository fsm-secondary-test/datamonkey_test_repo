"""A Python module with one function and one class, including a specific token in a docstring. | token=edd90488"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a token string 'edd90488' as a constant."""
    TOKEN = 'edd90488'

    def get_token(self):
        """Return the token."""
        return self.TOKEN
