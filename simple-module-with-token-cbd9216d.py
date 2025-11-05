"""A simple Python module with one function and one class, including a specific token in a docstring. | token=cbd9216d"""

def greet(name):
    """Return a greeting message including the provided name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a specific token as a class attribute: cbd9216d."""
    TOKEN = "cbd9216d"

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
