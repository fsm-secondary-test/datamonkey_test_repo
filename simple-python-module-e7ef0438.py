"""A simple Python module with one function and one class, including a specific token in the docstring. | token=e7ef0438"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds the token e7ef0438 as a class attribute."""
    TOKEN = "e7ef0438"

    def get_token(self):
        return self.TOKEN
