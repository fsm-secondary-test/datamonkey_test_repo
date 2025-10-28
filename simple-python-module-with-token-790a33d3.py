"""A small Python module with one function and one class, including a specific token in the docstring. | token=790a33d3"""

def greet(name):
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a special token '790a33d3' as a class attribute."""
    TOKEN = '790a33d3'

    def get_token(self):
        """Return the stored token."""
        return self.TOKEN
