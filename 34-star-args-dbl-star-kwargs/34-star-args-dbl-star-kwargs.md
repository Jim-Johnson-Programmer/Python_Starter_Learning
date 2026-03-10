# 34-star-args-dbl-star-kwargs

## Overview

This lesson covers \*args and \*\*kwargs, Python's special syntax for handling variable numbers of arguments in functions. These features allow functions to be more flexible and accept any number of arguments.

## Learning Objectives

- Understand what \*args and \*\*kwargs are and how they work
- Learn how to use \*args to accept variable positional arguments
- Learn how to use \*\*kwargs to accept variable keyword arguments
- Understand argument unpacking with \* and \*\*
- Recognize common use cases and best practices

## Code Examples

```python
# *args - variable positional arguments
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3))        # 6
print(sum_numbers(1, 2, 3, 4, 5))  # 15

# **kwargs - variable keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NYC")

# Using both together
def flexible_function(*args, **kwargs):
    print("Positional args:", args)
    print("Keyword args:", kwargs)

flexible_function(1, 2, 3, name="test", value=42)

# Argument unpacking
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(add(*numbers))  # Unpacks list into positional arguments

data = {"a": 10, "b": 20, "c": 30}
print(add(**data))    # Unpacks dict into keyword arguments
```

## Notes

- \*args collects extra positional arguments into a tuple
- \*\*kwargs collects extra keyword arguments into a dictionary
- The names 'args' and 'kwargs' are conventional but can be changed
- \*args must come before \*\*kwargs in function definitions
- Use these when you need flexible function signatures
- Argument unpacking (\*) works with any iterable, (\*\*) works with dictionaries
