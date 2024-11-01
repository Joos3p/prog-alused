"""Basic function exercises."""
import math

def print_hello():
    """Prints "Hello"."""
    print("Hello")

def get_hello() -> str:
    """Returns "Hello"."""
    return "Hello"

def ask_name_and_greet_user():
    """Asks for user's name and greets."""
    name = input("What's your name? ")
    if name.lower() == 'thanos':
        print("Get out of here, Thanos! Nobody wants to play with you!")
    else:
        print(f"Hi, {name.capitalize()}. Would you like to have a Hamburger?")

def calculate_hypotenuse_length(a: float, b: float) -> float:
    """Calculates and returns hypotenuse length."""
    return math.sqrt(a ** 2 + b ** 2)

def calculate_cathetus_length(a: float, c: float) -> float:
    """Calculates and returns cathetus length."""
    return math.sqrt(c ** 2 - a ** 2)

if __name__ == '__main__':
    print_hello()  
    hello = get_hello()  
    print(hello)  
    ask_name_and_greet_user()  
    print(calculate_hypotenuse_length(3, 4))  
    print(calculate_cathetus_length(3, 5))  
