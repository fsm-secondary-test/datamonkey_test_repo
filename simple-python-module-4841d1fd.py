"""A small Python module with one function and one class, including a specific token in the docstring. | token=4841d1fd"""

def greet(name):
    """Return a greeting string including the token 4841d1fd."""
    return f"Hello, {name}! Token: 4841d1fd"

class Counter:
    """Simple counter class with token 4841d1fd in docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
