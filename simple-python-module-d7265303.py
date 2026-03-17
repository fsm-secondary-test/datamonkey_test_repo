"""A small Python module with one function and one class, including a literal token in the docstring. | token=d7265303"""

def greet(name: str) -> str:
    """Return a greeting message including the given name.
    Token: d7265303
    """
    return f"Hello, {name}!"

class Counter:
    """A simple counter class.
    Token: d7265303
    """
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self) -> int:
        return self.count
