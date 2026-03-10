# 35-iterables
# Python learning exercise: Iterables

"""
WHAT ARE ITERABLES?
==================

Iterables are objects that can be iterated over - meaning you can loop through them.
In Python, an object is iterable if it implements the __iter__() method or has a __getitem__() method.

WHY ARE ITERABLES IMPORTANT?
===========================
- They allow you to process collections of data efficiently
- They work with for loops, list comprehensions, and many built-in functions
- They provide a consistent interface for different data types
- They enable lazy evaluation with generators

COMMON ITERABLE TYPES:
=====================
- Lists: [1, 2, 3]
- Tuples: (1, 2, 3)
- Strings: "hello"
- Dictionaries: {'key': 'value'}
- Sets: {1, 2, 3}
- Ranges: range(10)
- Files: open('file.txt')
- And many more!

KEY CONCEPT: ITERABLES vs ITERATORS
==================================
- Iterable: An object that can be iterated over (has __iter__ or __getitem__)
- Iterator: An object that keeps track of position during iteration (has __next__)
- Every iterator is also an iterable, but not vice versa
"""

def demonstrate_basic_iteration():
    """Show basic iteration over different iterable types."""
    print("=== Basic Iteration ===")

    # Lists
    fruits = ["apple", "banana", "cherry"]
    print("Iterating over a list:")
    for fruit in fruits:
        print(f"  {fruit}")

    # Tuples
    coordinates = (10, 20, 30)
    print("\nIterating over a tuple:")
    for coord in coordinates:
        print(f"  Coordinate: {coord}")

    # Strings
    message = "Hello"
    print("\nIterating over a string:")
    for char in message:
        print(f"  Character: {char}")

    # Sets
    colors = {"red", "green", "blue"}
    print("\nIterating over a set:")
    for color in colors:
        print(f"  Color: {color}")

    # Range
    print("\nIterating over a range:")
    for num in range(3):
        print(f"  Number: {num}")

def demonstrate_dictionary_iteration():
    """Show different ways to iterate over dictionaries."""
    print("\n=== Dictionary Iteration ===")

    person = {
        "name": "Alice",
        "age": 25,
        "city": "New York",
        "profession": "Engineer"
    }

    print("Iterating over keys (default):")
    for key in person:
        print(f"  {key}: {person[key]}")

    print("\nIterating over keys explicitly:")
    for key in person.keys():
        print(f"  {key}: {person[key]}")

    print("\nIterating over values:")
    for value in person.values():
        print(f"  Value: {value}")

    print("\nIterating over key-value pairs:")
    for key, value in person.items():
        print(f"  {key} -> {value}")

def demonstrate_built_in_functions():
    """Show built-in functions that work with iterables."""
    print("\n=== Built-in Functions for Iterables ===")

    numbers = [10, 5, 8, 3, 12, 7]

    print(f"Numbers: {numbers}")
    print(f"Length: {len(numbers)}")
    print(f"Sum: {sum(numbers)}")
    print(f"Maximum: {max(numbers)}")
    print(f"Minimum: {min(numbers)}")
    print(f"Sorted: {sorted(numbers)}")
    print(f"Reversed: {list(reversed(numbers))}")

    # Boolean functions
    print(f"All positive: {all(x > 0 for x in numbers)}")
    print(f"Any even: {any(x % 2 == 0 for x in numbers)}")

    # enumerate - iterate with index
    print("\nWith enumerate (index, value):")
    for index, value in enumerate(numbers):
        print(f"  Index {index}: {value}")

    # zip - iterate over multiple iterables
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]

    print("\nWith zip (parallel iteration):")
    for name, age in zip(names, ages):
        print(f"  {name} is {age} years old")

def demonstrate_list_comprehensions():
    """Show list comprehensions and related concepts."""
    print("\n=== List Comprehensions ===")

    # Basic list comprehension
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    squares = [x**2 for x in numbers]
    print(f"Squares: {squares}")

    # With condition
    even_squares = [x**2 for x in numbers if x % 2 == 0]
    print(f"Even squares: {even_squares}")

    # With transformation and condition
    descriptions = [f"{x} is {'even' if x % 2 == 0 else 'odd'}" for x in numbers]
    print(f"Descriptions: {descriptions}")

    # Nested comprehensions
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = [num for row in matrix for num in row]
    print(f"Flattened matrix: {flattened}")

    # Dictionary comprehension
    word_lengths = {word: len(word) for word in ["hello", "world", "python"]}
    print(f"Word lengths: {word_lengths}")

    # Set comprehension
    unique_lengths = {len(word) for word in ["hello", "world", "python", "hi"]}
    print(f"Unique lengths: {unique_lengths}")

def demonstrate_generator_expressions():
    """Show generator expressions (memory-efficient alternatives to lists)."""
    print("\n=== Generator Expressions ===")

    # Generator expression (parentheses instead of brackets)
    squares_gen = (x**2 for x in range(10))
    print(f"Generator object: {squares_gen}")

    # Convert to list to see values
    print(f"Squares from generator: {list(squares_gen)}")

    # Generators are memory efficient
    import sys

    # List comprehension creates entire list in memory
    list_comp = [x**2 for x in range(100000)]
    print(f"List comprehension memory: {sys.getsizeof(list_comp)} bytes")

    # Generator expression creates values on demand
    gen_expr = (x**2 for x in range(100000))
    print(f"Generator expression memory: {sys.getsizeof(gen_expr)} bytes")

    # Using generators with other functions
    even_squares_sum = sum(x**2 for x in range(10) if x % 2 == 0)
    print(f"Sum of even squares: {even_squares_sum}")

def demonstrate_iterable_vs_iterator():
    """Show the difference between iterables and iterators."""
    print("\n=== Iterables vs Iterators ===")

    # Lists are iterables (but not iterators)
    my_list = [1, 2, 3]
    print(f"List is iterable: {hasattr(my_list, '__iter__')}")
    print(f"List is iterator: {hasattr(my_list, '__next__')}")

    # Get an iterator from an iterable
    my_iterator = iter(my_list)
    print(f"Iterator is iterable: {hasattr(my_iterator, '__iter__')}")
    print(f"Iterator is iterator: {hasattr(my_iterator, '__next__')}")

    # Use the iterator
    print("Using iterator:")
    print(f"Next: {next(my_iterator)}")
    print(f"Next: {next(my_iterator)}")
    print(f"Next: {next(my_iterator)}")

    try:
        print(f"Next: {next(my_iterator)}")  # This will raise StopIteration
    except StopIteration:
        print("Iterator exhausted!")

class Countdown:
    """A custom iterable class that counts down from a number."""

    def __init__(self, start):
        self.start = start

    def __iter__(self):
        """Return an iterator object."""
        return CountdownIterator(self.start)

class CountdownIterator:
    """Iterator for the Countdown class."""

    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

def demonstrate_custom_iterable():
    """Show how to create custom iterable classes."""
    print("\n=== Custom Iterables ===")

    countdown = Countdown(5)
    print("Counting down from 5:")
    for number in countdown:
        print(f"  {number}")

    # Can iterate multiple times (each time creates new iterator)
    print("Counting down again:")
    for number in countdown:
        print(f"  {number}")

def main():
    print("=== Python Iterables Lesson ===\n")

    demonstrate_basic_iteration()
    demonstrate_dictionary_iteration()
    demonstrate_built_in_functions()
    demonstrate_list_comprehensions()
    demonstrate_generator_expressions()
    demonstrate_iterable_vs_iterator()
    demonstrate_custom_iterable()

    print("\n=== Summary ===")
    print("Iterables are everywhere in Python!")
    print("They enable clean, efficient data processing.")
    print("Master them and you'll write more Pythonic code.")

if __name__ == "__main__":
    main()
