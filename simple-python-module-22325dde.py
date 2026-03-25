"""A Python module with one function and one class including a specific token in a docstring. | token=22325dde"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a special token '22325dde' as a constant."""
    TOKEN = '22325dde'

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
