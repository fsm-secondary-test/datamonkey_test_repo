"""Datamonkey Test File 2

A Python file for testing GitHub sync with code content.
"""


def datamonkey_test_function():
    """Test function for datamonkey verification."""
    return "Hello from Datamonkey Test File 2!"


class DatamonkeyTestClass:
    """Test class for datamonkey verification."""
    
    def __init__(self):
        self.name = "Datamonkey Test Class"
        self.purpose = "Testing GitHub sync functionality"
    
    def get_info(self):
        """Get test class information."""
        return f"{self.name}: {self.purpose}"


if __name__ == "__main__":
    print(datamonkey_test_function())
    test_obj = DatamonkeyTestClass()
    print(test_obj.get_info())
