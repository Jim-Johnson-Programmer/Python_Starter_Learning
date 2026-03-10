# 39-modules
# Python learning exercise: Understanding modules

# First, let's create some example modules by writing to files
import os

# Create example modules
def create_example_modules():
    # Create mymodule.py
    mymodule_content = '''# mymodule.py - A simple example module
def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

def add_numbers(a, b):
    """Add two numbers."""
    return a + b

def multiply_numbers(a, b):
    """Multiply two numbers."""
    return a * b

PI = 3.14159
GRAVITY = 9.81

class Calculator:
    """A simple calculator class."""

    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def get_history(self):
        return self.history

def main():
    print("This function runs when mymodule.py is executed directly")

if __name__ == "__main__":
    main()
'''

    # Create math_utils.py
    math_utils_content = '''# math_utils.py - Mathematical utilities
import math

def calculate_circle_area(radius):
    """Calculate the area of a circle."""
    return math.pi * radius ** 2

def calculate_circle_circumference(radius):
    """Calculate the circumference of a circle."""
    return 2 * math.pi * radius

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def fibonacci(n):
    """Generate nth Fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

CONSTANTS = {
    'PI': math.pi,
    'E': math.e,
    'GOLDEN_RATIO': (1 + math.sqrt(5)) / 2
}
'''

    # Write the modules
    with open('mymodule.py', 'w') as f:
        f.write(mymodule_content)

    with open('math_utils.py', 'w') as f:
        f.write(math_utils_content)

    print("Example modules created!")

def main():
    print("=== Python Modules Tutorial ===\n")

    # Create example modules
    create_example_modules()
    print()

    # 1. Importing an entire module
    print("1. Importing an Entire Module:")
    import mymodule

    result = mymodule.add_numbers(5, 3)
    print(f"mymodule.add_numbers(5, 3) = {result}")

    greeting = mymodule.greet("Alice")
    print(f"mymodule.greet('Alice') = {greeting}")

    calc = mymodule.Calculator()
    calc_result = calc.add(4, 2)
    print(f"Calculator.add(4, 2) = {calc_result}")
    print(f"Calculator history: {calc.get_history()}")

    print(f"mymodule.PI = {mymodule.PI}")
    print()

    # 2. Importing specific items
    print("2. Importing Specific Items:")
    from mymodule import greet, multiply_numbers, PI

    greeting2 = greet("Bob")
    print(f"greet('Bob') = {greeting2}")

    multiply_result = multiply_numbers(4, 3)
    print(f"multiply_numbers(4, 3) = {multiply_result}")

    print(f"PI = {PI}")
    print()

    # 3. Importing with aliases
    print("3. Importing with Aliases:")
    import mymodule as mm
    from mymodule import greet as hello, add_numbers as add

    result3 = mm.multiply_numbers(6, 7)  # Using module alias
    print(f"mm.multiply_numbers(6, 7) = {result3}")

    greeting3 = hello("Charlie")  # Using function alias
    print(f"hello('Charlie') = {greeting3}")

    result4 = add(10, 20)  # Using function alias
    print(f"add(10, 20) = {result4}")
    print()

    # 4. Using built-in modules
    print("4. Using Built-in Modules:")
    import math
    import random
    import datetime

    print(f"math.sqrt(16) = {math.sqrt(16)}")
    print(f"math.pi = {math.pi:.5f}")

    random_num = random.randint(1, 10)
    print(f"random.randint(1, 10) = {random_num}")

    fruits = ['apple', 'banana', 'cherry', 'date']
    random_fruit = random.choice(fruits)
    print(f"random.choice({fruits}) = {random_fruit}")

    now = datetime.datetime.now()
    print(f"Current date and time: {now}")
    print(f"Current year: {now.year}")
    print()

    # 5. Using our custom math_utils module
    print("5. Using Custom math_utils Module:")
    import math_utils

    area = math_utils.calculate_circle_area(5)
    print(f"Circle area (radius 5) = {area:.2f}")

    circumference = math_utils.calculate_circle_circumference(5)
    print(f"Circle circumference (radius 5) = {circumference:.2f}")

    print(f"Is 17 prime? {math_utils.is_prime(17)}")
    print(f"Is 18 prime? {math_utils.is_prime(18)}")

    print(f"10th Fibonacci number: {math_utils.fibonacci(10)}")

    print(f"Mathematical constants: {math_utils.CONSTANTS}")
    print()

    # 6. Understanding __name__
    print("6. Understanding __name__:")
    print(f"Current module __name__: {__name__}")
    print(f"mymodule.__name__: {mymodule.__name__}")
    print(f"math_utils.__name__: {math_utils.__name__}")
    print()

    # 7. Module search path
    print("7. Module Search Path:")
    import sys
    print("Python module search paths:")
    for i, path in enumerate(sys.path[:3]):  # Show first 3 paths
        print(f"  {i+1}. {path}")
    if len(sys.path) > 3:
        print(f"  ... and {len(sys.path) - 3} more paths")
    print()

    # 8. Demonstrating the difference between modules, classes, and functions
    print("8. Modules vs Classes vs Functions:")

    # Function example
    def greet_function(name):
        return f"Hello, {name}! (from function)"

    print(f"Function call: {greet_function('Dave')}")

    # Class example
    class Greeter:
        def __init__(self, default_name="World"):
            self.default_name = default_name

        def greet(self, name=None):
            name = name or self.default_name
            return f"Hello, {name}! (from class method)"

    greeter = Greeter("ClassUser")
    print(f"Class method call: {greeter.greet()}")
    print(f"Class method call with arg: {greeter.greet('CustomName')}")

    # Module function (already demonstrated above)
    print(f"Module function call: {mymodule.greet('ModuleUser')}")

    print()

    # 9. Checking module attributes
    print("9. Module Attributes:")
    print(f"mymodule attributes: {[attr for attr in dir(mymodule) if not attr.startswith('_')]}")
    print(f"math attributes (first 10): {[attr for attr in dir(math) if not attr.startswith('_')][:10]}")
    print()

    # Clean up created files
    print("10. Cleaning up example modules:")
    try:
        os.remove('mymodule.py')
        os.remove('math_utils.py')
        print("Example modules removed.")
    except FileNotFoundError:
        print("Example modules not found (already removed).")

    print("\n=== End of Modules Tutorial ===")

if __name__ == "__main__":
    main()
