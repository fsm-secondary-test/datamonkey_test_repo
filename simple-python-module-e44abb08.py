"""A small Python module with one function and one class, including a literal token in a docstring. | token=e44abb08"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class to hold and display a special token e44abb08."""

    def __init__(self):
        self.token = 'e44abb08'

    def show_token(self):
        """Return the stored token."""
        return self.token
