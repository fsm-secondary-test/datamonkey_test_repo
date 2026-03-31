"""A Python module with one function and one class, including a specific token in a docstring. | token=0d8dc355"""

def greet(name):
    """Return a greeting message with the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class holding a special token 0d8dc355 in its docstring."""
    def __init__(self, token='0d8dc355'):
        self.token = token

    def get_token(self):
        return self.token
