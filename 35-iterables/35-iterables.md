# 35-iterables

## Overview

This lesson covers iterables in Python - objects that can be iterated over (looped through). Iterables are a fundamental concept in Python and include lists, tuples, strings, dictionaries, sets, and more.

## Learning Objectives

- Understand what iterables are and how they work
- Learn about common iterable types in Python
- Understand the difference between iterables and iterators
- Learn to use built-in functions that work with iterables
- Master list comprehensions and generator expressions
- Learn how to create custom iterable classes

## Code Examples

```python
# Common iterable types
my_list = [1, 2, 3, 4, 5]        # List
my_tuple = (1, 2, 3, 4, 5)       # Tuple
my_string = "Hello"               # String
my_dict = {'a': 1, 'b': 2}        # Dictionary
my_set = {1, 2, 3, 4, 5}         # Set
my_range = range(5)               # Range

# Iterating over iterables
for item in my_list:
    print(item)

for char in my_string:
    print(char)

# Built-in functions for iterables
print(len(my_list))      # Length
print(sum(my_list))      # Sum of elements
print(max(my_list))      # Maximum value
print(min(my_list))      # Minimum value

# List comprehensions
squares = [x**2 for x in range(10)]
even_squares = [x**2 for x in range(10) if x**2 % 2 == 0]

# Generator expressions (memory efficient)
squares_gen = (x**2 for x in range(10))
```

## Notes

- An iterable is any object that implements `__iter__()` or `__getitem__()`
- Iterables can be used with `for` loops, list comprehensions, and functions like `sum()`, `max()`, etc.
- Iterators are objects that keep track of their position during iteration
- List comprehensions create lists, generator expressions create iterators
- Common iterable types: list, tuple, string, dict, set, range, file objects
- Dictionaries iterate over keys by default, but you can iterate over values or items
