"""A small Python module containing one function and one class, including a literal token in a docstring. | token=c77a30e3"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class to hold and display a special token."""
    TOKEN = 'c77a30e3'
    
    def display_token(self):
        """Return the token string."""
        return self.TOKEN
