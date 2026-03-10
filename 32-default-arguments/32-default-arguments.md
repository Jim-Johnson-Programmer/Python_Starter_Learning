# 32-default-arguments

## Overview

This exercise demonstrates the use of default arguments in Python functions. Default arguments allow you to specify default values for function parameters, making them optional when calling the function.

## Learning Objectives

- Understand how to define functions with default arguments
- Learn how to call functions with and without providing values for default arguments
- Recognize the importance of default arguments for function flexibility

## Code Examples

```python
# Function with default arguments
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Calling with both arguments
print(greet("Alice", "Hi"))  # Output: Hi, Alice!

# Calling with only required argument (greeting uses default)
print(greet("Bob"))  # Output: Hello, Bob!

# Another example: a function to calculate area with default units
def calculate_area(length, width, unit="square meters"):
    area = length * width
    return f"The area is {area} {unit}."

print(calculate_area(5, 10))  # Uses default unit
print(calculate_area(5, 10, "square feet"))  # Overrides default
```

## Notes

- Default arguments must come after non-default arguments in the function definition.
- Default values are evaluated only once when the function is defined, not each time it's called.
- Be careful with mutable default arguments (like lists) as they can lead to unexpected behavior.
