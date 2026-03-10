# 36-membership-operators

## Overview

Membership operators in Python are used to test whether a value is a member of a sequence (such as strings, lists, tuples, sets, or dictionaries). The two membership operators are `in` and `not in`. These operators return boolean values (True or False) and are commonly used for checking presence or absence of elements in collections.

## Learning Objectives

- Understand what membership operators are and how they work
- Learn the syntax and usage of `in` and `not in` operators
- Explore how membership operators work with different data types (strings, lists, tuples, sets, dictionaries)
- Practice using membership operators in conditional statements
- Understand the efficiency and use cases of membership operators

## Code Examples

### Basic Usage with Lists

```python
# Using 'in' operator with lists
fruits = ['apple', 'banana', 'cherry', 'date']

print('apple' in fruits)      # True
print('grape' in fruits)      # False

# Using 'not in' operator with lists
print('grape' not in fruits)  # True
print('apple' not in fruits)  # False
```

### Working with Strings

```python
# Membership operators work with substrings
text = "Hello, World!"

print('Hello' in text)        # True
print('hello' in text)        # False (case-sensitive)
print('World' in text)        # True
print('Python' in text)       # False

print('Python' not in text)   # True
```

### Using with Tuples

```python
# Tuples support membership operators
coordinates = (10, 20, 30, 40)

print(20 in coordinates)      # True
print(50 in coordinates)      # False
print(50 not in coordinates)  # True
```

### Working with Sets

```python
# Sets are optimized for membership testing
numbers = {1, 2, 3, 4, 5}

print(3 in numbers)           # True
print(6 in numbers)           # False

# Sets are very fast for membership testing
large_set = set(range(100000))
print(99999 in large_set)     # True (very fast operation)
```

### Dictionary Membership Testing

```python
# 'in' checks for keys in dictionaries
student_grades = {'Alice': 95, 'Bob': 87, 'Charlie': 92}

print('Alice' in student_grades)      # True
print('David' in student_grades)      # False

# To check values, use .values()
print(95 in student_grades.values())  # True
print(100 in student_grades.values()) # False
```

### Using in Conditional Statements

```python
def check_vowel(char):
    vowels = 'aeiouAEIOU'
    if char in vowels:
        return f"'{char}' is a vowel"
    else:
        return f"'{char}' is not a vowel"

print(check_vowel('a'))  # 'a' is a vowel
print(check_vowel('b'))  # 'b' is not a vowel

# Checking multiple conditions
def categorize_character(char):
    if char in 'aeiouAEIOU':
        return "Vowel"
    elif char in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
        return "Consonant"
    elif char in '0123456789':
        return "Digit"
    else:
        return "Special character"

print(categorize_character('A'))  # Vowel
print(categorize_character('3'))  # Digit
print(categorize_character('@'))  # Special character
```

### Practical Examples

```python
# Checking user permissions
user_roles = ['admin', 'editor', 'viewer']

def has_access(user_role, required_role):
    return user_role in user_roles and user_role == required_role or user_role == 'admin'

print(has_access('admin', 'editor'))  # True (admin has all access)
print(has_access('viewer', 'editor')) # False

# Filtering data
data = [10, 20, 30, 40, 50]
allowed_values = [20, 30, 40]

filtered_data = [x for x in data if x in allowed_values]
print(filtered_data)  # [20, 30, 40]

# Checking for forbidden items
shopping_cart = ['apple', 'banana', 'cherry']
forbidden_items = ['cherry', 'date']

has_forbidden = any(item in forbidden_items for item in shopping_cart)
print(f"Cart has forbidden items: {has_forbidden}")  # True
```

## Notes

- Membership operators return boolean values (True/False)
- `in` returns True if the value is found in the sequence
- `not in` returns True if the value is NOT found in the sequence
- Works with all sequence types: strings, lists, tuples, sets, dictionaries (keys only)
- Case-sensitive for strings
- Sets and dictionaries provide O(1) average time complexity for membership testing
- Lists and tuples require O(n) time complexity (linear search)
- Commonly used in conditional statements and list comprehensions
- Can be combined with other operators using `and`, `or`, `not`
