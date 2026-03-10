# 41-if-name-eq-main
# Understanding if __name__ == '__main__'

def main():
    print("=== if __name__ == '__main__' Tutorial ===\n")

    # Section 1: Basic __name__ understanding
    print("1. Understanding __name__")
    basic_name_demo()
    print()

    # Section 2: Script vs Module behavior
    print("2. Script vs Module Behavior")
    script_module_demo()
    print()

    # Section 3: Calculator example
    print("3. Calculator as Script and Module")
    calculator_demo()
    print()

    # Section 4: Math utilities with tests
    print("4. Math Utilities with Built-in Tests")
    math_utils_demo()
    print()

    # Section 5: Command line interface
    print("5. Command Line Interface Pattern")
    cli_demo()
    print()

    # Section 6: Avoiding global execution
    print("6. Avoiding Global Code Execution")
    global_execution_demo()
    print()

def basic_name_demo():
    """Demonstrate what __name__ contains"""
    print(f"Current __name__: {__name__}")
    print("This shows whether this file was run directly or imported")

    # Show how __name__ changes
    print("\nWhen run directly: __name__ = '__main__'")
    print("When imported: __name__ = '41-if-name-eq-main'")

def script_module_demo():
    """Show the difference between running as script vs importing as module"""
    print("This function demonstrates script vs module behavior")

    # This code structure allows the file to be both:
    # 1. A script that can be run directly
    # 2. A module that can be imported by other scripts

    print("✓ This code can be executed directly")
    print("✓ Functions can be imported by other modules")
    print("✓ No unintended side effects when imported")

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract two numbers"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def calculator_demo():
    """Demonstrate calculator that works as both script and module"""
    print("Calculator functions available:")
    print(f"add(5, 3) = {add(5, 3)}")
    print(f"subtract(10, 4) = {subtract(10, 4)}")
    print(f"multiply(6, 7) = {multiply(6, 7)}")
    print(f"divide(15, 3) = {divide(15, 3)}")

    print("\nThis calculator can be used in two ways:")
    print("1. Import functions: from calculator import add, multiply")
    print("2. Run as script: python calculator.py add 5 3")

def fibonacci(n):
    """Calculate the nth Fibonacci number"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def is_prime(n):
    """Check if a number is prime"""
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

def factorial(n):
    """Calculate factorial of n"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def math_utils_demo():
    """Demonstrate math utilities with built-in tests"""
    print("Testing Fibonacci function:")
    for i in range(8):
        print(f"F({i}) = {fibonacci(i)}")

    print("\nTesting prime numbers (1-20):")
    primes = [i for i in range(2, 21) if is_prime(i)]
    print(f"Prime numbers: {primes}")

    print("\nTesting factorial function:")
    for i in range(6):
        print(f"{i}! = {factorial(i)}")

def process_text(text, operation):
    """Process text based on operation"""
    if operation == 'uppercase':
        return text.upper()
    elif operation == 'lowercase':
        return text.lower()
    elif operation == 'reverse':
        return text[::-1]
    elif operation == 'length':
        return str(len(text))
    else:
        return text

def cli_demo():
    """Demonstrate command line interface pattern"""
    import sys

    print("Command Line Interface Example")
    print("This would normally parse command line arguments")

    # Simulate some command line operations
    test_text = "Hello, World!"

    print(f"\nOriginal text: {test_text}")
    print(f"Uppercase: {process_text(test_text, 'uppercase')}")
    print(f"Lowercase: {process_text(test_text, 'lowercase')}")
    print(f"Reverse: {process_text(test_text, 'reverse')}")
    print(f"Length: {process_text(test_text, 'length')}")

    print("\nIn a real CLI, you would use:")
    print("python script.py uppercase 'Hello World'")
    print("sys.argv would contain: ['script.py', 'uppercase', 'Hello World']")

def demonstrate_import_behavior():
    """This function shows what happens when imported"""
    print("This function was called from an imported module")
    return "Import successful"

def global_execution_demo():
    """Demonstrate avoiding global code execution"""
    print("This demonstrates proper use of if __name__ == '__main__'")

    # This function can be imported and used by other modules
    # without executing the main demonstration code

    print("✓ Functions are available for import")
    print("✓ No global code execution when imported")
    print("✓ Clean separation between library and script functionality")

# This block only executes when the script is run directly
if __name__ == '__main__':
    main()
