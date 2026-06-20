"""
This is my app!!!
"""

def hello(name: str,age: int) -> str:
    """
    This function takes a name and an age as input and returns a greeting message.
    """
    return f"Hello {name}, you are {age} years old!"

if __name__ == "__main__":
    print(hello("Alice", 30))
    print(hello("Bob", 25))
    print(hello("Charlie", 35))