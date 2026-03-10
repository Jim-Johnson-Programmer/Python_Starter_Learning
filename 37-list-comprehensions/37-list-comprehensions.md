# 37-list-comprehensions

## Overview

List comprehensions are a concise and elegant way to create lists in Python. They provide a compact syntax for creating new lists by applying an expression to each item in an iterable (like a list, tuple, or range) and optionally filtering items with a condition. List comprehensions are more readable and often more efficient than traditional for loops for creating lists.

## Learning Objectives

- Understand the basic syntax of list comprehensions
- Learn how to use conditional statements in list comprehensions
- Explore nested list comprehensions
- Practice using list comprehensions with multiple iterables
- Compare list comprehensions with equivalent for loop implementations
- Learn about related comprehensions (dictionary and set comprehensions)

## Code Examples

### Basic List Comprehension

```python
# Traditional for loop approach
numbers = [1, 2, 3, 4, 5]
squares = []
for num in numbers:
    squares.append(num ** 2)

# List comprehension approach
squares = [num ** 2 for num in numbers]
# Result: [1, 4, 9, 16, 25]
```

### List Comprehension with Expression

```python
# Create a list of strings from numbers
numbers = [1, 2, 3, 4, 5]
string_numbers = [str(num) for num in numbers]
# Result: ['1', '2', '3', '4', '5']

# Apply functions to each element
words = ['hello', 'world', 'python']
upper_words = [word.upper() for word in words]
# Result: ['HELLO', 'WORLD', 'PYTHON']
```

### List Comprehension with Condition (Filtering)

```python
# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
# Result: [2, 4, 6, 8, 10]

# Filter with multiple conditions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered = [num for num in numbers if num > 3 and num % 2 == 0]
# Result: [4, 6, 8, 10]
```

### List Comprehension with if-else (Conditional Expression)

```python
# Categorize numbers as even or odd
numbers = [1, 2, 3, 4, 5]
categories = ['even' if num % 2 == 0 else 'odd' for num in numbers]
# Result: ['odd', 'even', 'odd', 'even', 'odd']

# Transform with condition
numbers = [1, 2, 3, 4, 5]
transformed = [num * 2 if num % 2 == 0 else num for num in numbers]
# Result: [1, 4, 3, 8, 5]
```

### Nested List Comprehensions

```python
# Flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
# Result: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create a multiplication table
table = [[i * j for j in range(1, 4)] for i in range(1, 4)]
# Result: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

### List Comprehension with Multiple Iterables

```python
# Using zip with list comprehension
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
people = [f"{name} is {age} years old" for name, age in zip(names, ages)]
# Result: ['Alice is 25 years old', 'Bob is 30 years old', 'Charlie is 35 years old']
```

### Working with Strings

```python
# Split and filter words
sentence = "The quick brown fox jumps over the lazy dog"
words = sentence.split()
long_words = [word for word in words if len(word) > 3]
# Result: ['quick', 'brown', 'jumps', 'over', 'lazy']

# Extract vowels from a string
text = "Hello World"
vowels = [char for char in text if char.lower() in 'aeiou']
# Result: ['e', 'o', 'o']
```

### Dictionary Comprehensions (Related)

```python
# Create dictionary from two lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dict_comp = {key: value for key, value in zip(keys, values)}
# Result: {'a': 1, 'b': 2, 'c': 3}

# Filter dictionary
original = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered_dict = {k: v for k, v in original.items() if v > 2}
# Result: {'c': 3, 'd': 4}
```

### Set Comprehensions (Related)

```python
# Create set from list (removes duplicates)
numbers = [1, 2, 2, 3, 3, 3, 4]
unique_squares = {num ** 2 for num in numbers}
# Result: {1, 4, 9, 16}

# Filter set
numbers = {1, 2, 3, 4, 5, 6}
even_squares = {num ** 2 for num in numbers if num % 2 == 0}
# Result: {4, 16, 36}
```

### Practical Examples

```python
# Read and process file data
# lines = [line.strip() for line in open('file.txt') if line.strip()]

# Process CSV-like data
data = ["Name,Age,City", "Alice,25,NYC", "Bob,30,LA", "Charlie,35,Chicago"]
# Extract ages as integers
ages = [int(line.split(',')[1]) for line in data[1:]]
# Result: [25, 30, 35]

# Find all files with specific extension
import os
# files = [f for f in os.listdir('.') if f.endswith('.py')]

# Matrix operations
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Get diagonal elements
diagonal = [matrix[i][i] for i in range(len(matrix))]
# Result: [1, 5, 9]
```

## Notes

- List comprehensions are more concise than traditional for loops
- They are generally faster than equivalent for loop implementations
- Use parentheses `()` for generator expressions (lazy evaluation)
- Use square brackets `[]` for list comprehensions (eager evaluation)
- Complex comprehensions can reduce readability - consider using regular loops for complex logic
- List comprehensions can include multiple for clauses and conditions
- Related comprehensions: dict comprehensions use `{}`, set comprehensions use `{}`, generator expressions use `()`
- Always consider readability - sometimes a regular loop is clearer than a complex comprehension
