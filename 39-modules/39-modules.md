# 39-modules

## Overview

Modules in Python are files containing Python code that can define functions, classes, and variables. They allow you to organize code into reusable components and avoid code duplication. Modules can be imported into other Python programs, making it easier to build complex applications by breaking them down into smaller, manageable pieces.

## Learning Objectives

- Understand what modules are and why they are useful
- Learn how to create and use custom modules
- Master different ways to import modules and their contents
- Explore built-in modules and the standard library
- Understand the difference between modules, classes, and functions
- Learn about packages and how they relate to modules

## Code Examples

### Creating a Simple Module

```python
# mymodule.py
def greet(name):
    return f"Hello, {name}!"

def add_numbers(a, b):
    return a + b

PI = 3.14159

class Calculator:
    def multiply(self, a, b):
        return a * b
```

### Importing an Entire Module

```python
import mymodule

result = mymodule.add_numbers(5, 3)
print(result)  # 8

greeting = mymodule.greet("Alice")
print(greeting)  # "Hello, Alice!"

calc = mymodule.Calculator()
print(calc.multiply(4, 2))  # 8

print(mymodule.PI)  # 3.14159
```

### Importing Specific Items

```python
from mymodule import greet, add_numbers

result = add_numbers(5, 3)
print(result)  # 8

greeting = greet("Bob")
print(greeting)  # "Hello, Bob!"
```

### Importing with Aliases

```python
import mymodule as mm
from mymodule import greet as hello, add_numbers as add

result = mm.add_numbers(5, 3)  # Using module alias
print(result)  # 8

greeting = hello("Charlie")  # Using function alias
print(greeting)  # "Hello, Charlie!"
```

### Using Built-in Modules

```python
import math
import random
import datetime

# Math module
print(math.sqrt(16))  # 4.0
print(math.pi)  # 3.141592653589793

# Random module
print(random.randint(1, 10))  # Random integer between 1 and 10
print(random.choice(['apple', 'banana', 'cherry']))  # Random choice

# Datetime module
now = datetime.datetime.now()
print(now)  # Current date and time
print(now.year)  # Current year
```

### The **name** Variable

```python
# In mymodule.py
def main():
    print("This is the main function in mymodule")

if __name__ == "__main__":
    main()
    print("mymodule is being run directly")
else:
    print("mymodule has been imported")
```

### Module Search Path

```python
import sys

print(sys.path)  # List of directories where Python looks for modules

# You can add custom paths
sys.path.append('/path/to/your/modules')
```

### Creating a Package

```
mypackage/
├── __init__.py
├── module1.py
└── module2.py
```

```python
# mypackage/__init__.py
from .module1 import function1
from .module2 import function2

# Usage
import mypackage
mypackage.function1()
```

## Modules vs Classes vs Functions

### Functions

- **Definition**: Blocks of reusable code that perform specific tasks
- **Purpose**: Execute operations and optionally return values
- **Scope**: Local variables, can access global variables
- **Usage**: Called to perform actions or compute values
- **Example**:

```python
def greet(name):
    return f"Hello, {name}!"
```

### Classes

- **Definition**: Blueprints for creating objects with attributes and methods
- **Purpose**: Model real-world entities and their behaviors
- **Scope**: Instance variables (self), class variables
- **Usage**: Create instances (objects) with shared behavior
- **Example**:

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I'm {self.name}!"
```

### Modules

- **Definition**: Files containing Python code (functions, classes, variables)
- **Purpose**: Organize and reuse code across multiple programs
- **Scope**: Module-level variables and functions
- **Usage**: Import and use code from other files
- **Example**:

```python
# person.py (module)
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I'm {self.name}!"

def create_person(name):
    return Person(name)
```

### Key Differences

| Aspect            | Function              | Class                   | Module                 |
| ----------------- | --------------------- | ----------------------- | ---------------------- |
| **Purpose**       | Perform specific task | Model entities/behavior | Organize reusable code |
| **Instantiation** | Called directly       | Create objects          | Import into programs   |
| **Scope**         | Function scope        | Instance/Class scope    | Module scope           |
| **Reusability**   | Within program        | Multiple instances      | Across programs        |
| **Organization**  | Single operation      | Related data/methods    | Related functionality  |
| **Import**        | N/A                   | N/A                     | `import module`        |
| **Execution**     | When called           | Through methods         | When imported/run      |

## Notes

- Modules help organize code and promote reusability
- Use `import` for entire modules, `from import` for specific items
- The `__name__` variable helps distinguish between direct execution and importing
- Python's standard library contains many useful built-in modules
- Packages are directories containing multiple modules with `__init__.py`
- Modules are cached after first import for performance
- Use relative imports within packages: `from .module import function`
- Avoid circular imports by restructuring your code organization
