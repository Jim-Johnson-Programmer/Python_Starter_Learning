# 33-keyword-arguments

## Overview

This exercise demonstrates the use of keyword arguments in Python functions. Keyword arguments allow you to pass arguments by explicitly naming the parameters, making function calls more readable and flexible.

## Learning Objectives

- Understand how to use keyword arguments when calling functions
- Learn the difference between positional and keyword arguments
- Recognize when to use keyword arguments for code clarity
- Understand the rules for mixing positional and keyword arguments

## Code Examples

```python
# Function definition
def describe_person(name, age, city):
    return f"{name} is {age} years old and lives in {city}."

# Using positional arguments
print(describe_person("Alice", 25, "New York"))

# Using keyword arguments (order doesn't matter)
print(describe_person(age=30, name="Bob", city="London"))
print(describe_person(city="Paris", name="Charlie", age=35))

# Mixing positional and keyword arguments
# Positional arguments must come first
print(describe_person("David", age=40, city="Tokyo"))
```

## Notes

- Keyword arguments are specified with `parameter_name=value`
- When using keyword arguments, the order doesn't matter
- You can mix positional and keyword arguments, but positional arguments must come first
- Keyword arguments improve code readability, especially with functions that have many parameters
- All arguments after the first keyword argument must also be keyword arguments
