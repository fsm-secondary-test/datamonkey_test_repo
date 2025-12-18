"""A small Python module with one function and one class, including a literal token in a docstring. | token=2141fa86"""

def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

class TokenHolder:
    """Class that holds a token string: '2141fa86'."""
    def __init__(self):
        self.token = '2141fa86'
    
    def get_token(self):
        return self.token
