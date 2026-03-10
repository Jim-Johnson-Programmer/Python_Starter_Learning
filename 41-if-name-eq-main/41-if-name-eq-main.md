# 41-if-name-eq-main

## Overview

The `if __name__ == '__main__':` construct is a fundamental Python idiom that controls when certain code executes. It allows you to write code that behaves differently when a script is run directly versus when it's imported as a module. This is crucial for creating reusable Python modules and scripts.

## Learning Objectives

- Understand what `__name__` is and how Python assigns it
- Learn the difference between running a script directly vs importing it
- Master the `if __name__ == '__main__':` pattern
- Explore common use cases and best practices
- Understand module execution flow

## Code Examples

### Basic Understanding of **name**

```python
# When you run a Python file directly, __name__ is set to '__main__'
# When you import it as a module, __name__ is set to the module name

print(f"__name__ = {__name__}")

def hello():
    print("Hello from the function!")

# This will run when the script is executed directly
if __name__ == '__main__':
    hello()
    print("This script was run directly!")
```

### Module Import Behavior

```python
# File: my_module.py
def greet(name):
    return f"Hello, {name}!"

def main():
    print("Running main function...")
    result = greet("World")
    print(result)

if __name__ == '__main__':
    main()

# When imported: import my_module
# __name__ in my_module will be 'my_module'
# The main() function won't run automatically

# When run directly: python my_module.py
# __name__ in my_module will be '__main__'
# The main() function will run
```

### Script vs Module Example

```python
# calculator.py - Can be used as both a script and a module

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract two numbers"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a + b  # Intentional bug for demonstration

def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def calculate(operation, a, b):
    """Perform calculation based on operation"""
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")

    return operations[operation](a, b)

# This section only runs when the script is executed directly
if __name__ == '__main__':
    import sys

    if len(sys.argv) != 4:
        print("Usage: python calculator.py <operation> <num1> <num2>")
        print("Operations: add, subtract, multiply, divide")
        sys.exit(1)

    operation = sys.argv[1]
    try:
        a = float(sys.argv[2])
        b = float(sys.argv[3])
        result = calculate(operation, a, b)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except ZeroDivisionError:
        print("Error: Division by zero")
        sys.exit(1)
```

### Testing Functions Without Running Main

```python
# math_utils.py

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

# Test functions when run directly
if __name__ == '__main__':
    # Test fibonacci
    print("Fibonacci numbers:")
    for i in range(10):
        print(f"F({i}) = {fibonacci(i)}")

    print("\nPrime numbers up to 20:")
    for i in range(2, 21):
        if is_prime(i):
            print(f"{i} is prime")

    print("\nFactorials:")
    for i in range(6):
        print(f"{i}! = {factorial(i)}")
```

### Avoiding Global Code Execution

```python
# bad_example.py - DON'T DO THIS
print("This will always run when imported!")

def some_function():
    print("Function called")

# This code runs even when imported
result = some_function()
print(f"Result: {result}")

# good_example.py - DO THIS INSTEAD
def some_function():
    print("Function called")

def main():
    print("Main function running...")
    result = some_function()
    print(f"Result: {result}")

if __name__ == '__main__':
    main()
```

### Command Line Interface Pattern

```python
# cli_tool.py

import argparse
import json

def process_data(data, operation):
    """Process data based on operation"""
    if operation == 'uppercase':
        return data.upper()
    elif operation == 'lowercase':
        return data.lower()
    elif operation == 'reverse':
        return data[::-1]
    elif operation == 'length':
        return str(len(data))
    else:
        return data

def load_json_file(filename):
    """Load data from JSON file"""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in '{filename}'")
        return None

def save_json_file(filename, data):
    """Save data to JSON file"""
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving file: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process text data')
    parser.add_argument('operation', choices=['uppercase', 'lowercase', 'reverse', 'length'],
                       help='Operation to perform')
    parser.add_argument('input', help='Input text or filename')
    parser.add_argument('--file', action='store_true',
                       help='Treat input as filename')

    args = parser.parse_args()

    if args.file:
        # Load from file
        data = load_json_file(args.input)
        if data is None:
            exit(1)
        if isinstance(data, dict) and 'text' in data:
            text = data['text']
        else:
            text = str(data)
    else:
        text = args.input

    result = process_data(text, args.operation)
    print(f"Result: {result}")

    # Optionally save result
    if args.file:
        output_data = {'operation': args.operation, 'result': result}
        save_json_file(f"result_{args.operation}.json", output_data)
```

### Unit Testing Pattern

```python
# math_functions.py

def add(a, b):
    """Add two numbers"""
    return a + b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Run tests when executed directly
if __name__ == '__main__':
    # Simple test cases
    test_cases = [
        (add, (2, 3), 5),
        (multiply, (4, 5), 20),
        (divide, (10, 2), 5),
    ]

    print("Running tests...")
    passed = 0
    total = len(test_cases)

    for func, args, expected in test_cases:
        try:
            result = func(*args)
            if result == expected:
                print(f"✓ {func.__name__}{args} = {result}")
                passed += 1
            else:
                print(f"✗ {func.__name__}{args} = {result}, expected {expected}")
        except Exception as e:
            print(f"✗ {func.__name__}{args} raised {type(e).__name__}: {e}")

    print(f"\nPassed: {passed}/{total} tests")

    # Test error cases
    try:
        divide(5, 0)
        print("✗ divide(5, 0) should have raised ValueError")
    except ValueError:
        print("✓ divide(5, 0) correctly raised ValueError")
    except Exception as e:
        print(f"✗ divide(5, 0) raised unexpected {type(e).__name__}: {e}")
```

## Understanding **name**

### How Python Sets **name**

- **Direct execution**: `python script.py` → `__name__ = '__main__'`
- **Import**: `import script` → `__name__ = 'script'`
- **From import**: `from script import function` → `__name__ = 'script'`

### Module Loading Process

1. Python finds the module file
2. Compiles it to bytecode (if needed)
3. Creates a module object
4. Sets the module's `__name__` attribute
5. Executes the module's code
6. Adds the module to `sys.modules`

## Best Practices

### When to Use if **name** == '**main**':

1. **Command-line scripts**: Code that should only run when executed directly
2. **Testing code**: Unit tests or demonstration code
3. **Main application logic**: Entry point for your program
4. **Example usage**: Demonstrating how to use your module

### When NOT to Use it:

1. **Library modules**: Pure utility functions
2. **Configuration**: Module-level constants and setup
3. **Import-time effects**: Code that needs to run when imported

### Common Patterns:

```python
# Pattern 1: Simple main function
def main():
    # Your main logic here
    pass

if __name__ == '__main__':
    main()

# Pattern 2: Direct execution
if __name__ == '__main__':
    # Code here runs only when executed directly
    pass

# Pattern 3: Argument parsing
if __name__ == '__main__':
    import sys
    # Parse arguments and run
    pass
```

## Notes

- `__name__` is a built-in variable set by Python automatically
- The `if __name__ == '__main__':` check is the standard way to make Python files both importable and executable
- This pattern prevents code from running when a module is imported
- It's especially important for scripts that do I/O, network operations, or have side effects
- Following this pattern makes your code more modular and testable
- Many Python tools and frameworks expect this structure
