# 53-oop-static-methods

## Overview

Static methods in Python are methods that belong to a class rather than an instance of the class. They are defined using the `@staticmethod` decorator and do not have access to `self` or `cls`. Static methods are useful for utility functions that perform operations related to the class but don't need to access instance or class variables.

## Learning Objectives

- Understand what static methods are and how they differ from instance and class methods
- Learn when and why to use static methods
- Master the syntax for defining and calling static methods
- Explore practical use cases for static methods in Python classes

## Code Examples

### Basic Static Method Definition

```python
class MathUtils:
    @staticmethod
    def add_numbers(a, b):
        return a + b

    @staticmethod
    def multiply_numbers(a, b):
        return a * b

# Calling static methods
result1 = MathUtils.add_numbers(5, 3)  # Returns 8
result2 = MathUtils.multiply_numbers(4, 2)  # Returns 8
```

### Static Method for Utility Functions

```python
class StringHelper:
    @staticmethod
    def is_palindrome(text):
        cleaned = ''.join(c.lower() for c in text if c.isalnum())
        return cleaned == cleaned[::-1]

    @staticmethod
    def count_words(text):
        return len(text.split())

# Usage
print(StringHelper.is_palindrome("A man, a plan, a canal: Panama"))  # True
print(StringHelper.count_words("Hello world from Python"))  # 4
```

### Static Method in a Class with Instance Methods

```python
class TemperatureConverter:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

# Instance method usage
converter = TemperatureConverter(25)
print(converter.to_fahrenheit())  # 77.0

# Static method usage
print(TemperatureConverter.celsius_to_fahrenheit(25))  # 77.0
print(TemperatureConverter.fahrenheit_to_celsius(77))  # 25.0
```

### Static Method for Validation

```python
class UserValidator:
    @staticmethod
    def is_valid_email(email):
        return '@' in email and '.' in email.split('@')[1]

    @staticmethod
    def is_valid_password(password):
        return len(password) >= 8 and any(c.isdigit() for c in password)

# Usage
print(UserValidator.is_valid_email("user@example.com"))  # True
print(UserValidator.is_valid_password("password123"))  # True
```

## Notes

- Static methods are called on the class, not on instances
- They don't have access to `self` or `cls` parameters
- Use static methods when the function is logically related to the class but doesn't need instance data
- Common use cases: utility functions, factory methods, validation functions
- Static methods can be inherited by subclasses
- They can be overridden in subclasses like regular methods
