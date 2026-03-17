"""A small Python module with one function and one class, including a specific token in the docstring. | token=b6e10765"""

def greet(name):
    """Return a greeting message including the token b6e10765."""
    return f"Hello, {name}! Welcome to the module with token b6e10765."

class Counter:
    """A simple counter class that includes token b6e10765 in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by 1."""
        self.count += 1

    def get_count(self):
        """Return the current count."""
        return self.count
