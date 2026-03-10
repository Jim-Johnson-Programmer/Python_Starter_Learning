# 40-scope-resolution

## Overview

Scope resolution in Python refers to the rules that determine which variables and functions are accessible at different points in your code. Python uses the LEGB rule (Local, Enclosing, Global, Built-in) to resolve variable names. Understanding scope is crucial for writing clean, bug-free code and avoiding common errors like UnboundLocalError.

## Learning Objectives

- Understand the LEGB rule and scope hierarchy
- Learn how variables are resolved in different scopes
- Master the use of `global` and `nonlocal` keywords
- Explore scope behavior in nested functions and classes
- Identify and fix common scope-related errors

## Code Examples

### LEGB Rule Overview

```python
# Built-in scope (B) - Available everywhere
print(len("hello"))  # len is a built-in function

# Global scope (G) - Module level variables
global_var = "I'm global"

def outer_function():
    # Enclosing scope (E) - Variables in outer functions
    enclosing_var = "I'm enclosing"

    def inner_function():
        # Local scope (L) - Variables defined in current function
        local_var = "I'm local"

        print(local_var)      # Local scope
        print(enclosing_var)  # Enclosing scope
        print(global_var)     # Global scope
        print(len("test"))    # Built-in scope

    inner_function()

outer_function()
```

### Local Scope

```python
def local_scope_example():
    x = 10  # Local variable
    print(f"Inside function: x = {x}")

x = 5  # Global variable
local_scope_example()  # Prints: Inside function: x = 10
print(f"Outside function: x = {x}")  # Prints: Outside function: x = 5
```

### Enclosing Scope (Nested Functions)

```python
def outer():
    x = "outer"

    def inner():
        x = "inner"
        print(f"Inner function: x = {x}")

    inner()
    print(f"Outer function: x = {x}")

outer()
# Output:
# Inner function: x = inner
# Outer function: x = outer
```

### Global Scope

```python
# Global variables
counter = 0

def increment_counter():
    global counter  # Declare that we're using the global variable
    counter += 1
    print(f"Counter: {counter}")

increment_counter()  # Counter: 1
increment_counter()  # Counter: 2
print(f"Global counter: {counter}")  # Global counter: 2
```

### Built-in Scope

```python
# Built-in functions are always available
print(max([1, 2, 3]))  # 3
print(min([1, 2, 3]))  # 1
print(sum([1, 2, 3]))  # 6

# You can shadow built-in names (not recommended)
def max(a, b):  # This shadows the built-in max function
    return a if a > b else b

print(max(5, 10))  # 10 (our function, not built-in)
```

### The global Keyword

```python
x = 10  # Global variable

def modify_global():
    global x  # Without this, we'd get UnboundLocalError
    x = 20

def try_modify_global():
    # x = 30  # This would create a local x instead
    global x
    x = 30

print(f"Initial x: {x}")  # 10
modify_global()
print(f"After modify_global: {x}")  # 20
try_modify_global()
print(f"After try_modify_global: {x}")  # 30
```

### The nonlocal Keyword

```python
def outer():
    x = "outer"

    def middle():
        x = "middle"

        def inner():
            nonlocal x  # Refers to x in middle(), not outer()
            x = "modified by inner"

        print(f"Before inner: x = {x}")
        inner()
        print(f"After inner: x = {x}")

    middle()
    print(f"Outer x: {x}")

outer()
# Output:
# Before inner: x = middle
# After inner: x = modified by inner
# Outer x: outer
```

### Scope Resolution Order

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(f"Local x: {x}")

        # Access enclosing scope
        def innermost():
            print(f"Enclosing x: {x}")  # Refers to inner's x

        innermost()

    inner()

outer()
```

### Classes and Scope

```python
class ScopeExample:
    class_var = "class variable"

    def __init__(self):
        self.instance_var = "instance variable"

    def method(self):
        local_var = "local variable"
        print(f"Local: {local_var}")
        print(f"Instance: {self.instance_var}")
        print(f"Class: {self.class_var}")
        print(f"Global: {globals().get('x', 'not found')}")

# Global variable
x = "global"

obj = ScopeExample()
obj.method()
```

### Common Scope Errors and Solutions

```python
# Error 1: UnboundLocalError
x = 10

def problematic():
    print(x)  # This would work
    x = 20    # But this assignment makes x local, causing UnboundLocalError

# Solution: Use global keyword
def correct():
    global x
    print(x)
    x = 20

# Error 2: Trying to modify enclosing variable
def outer():
    x = 10

    def inner():
        x += 1  # UnboundLocalError

# Solution: Use nonlocal
def outer_fixed():
    x = 10

    def inner():
        nonlocal x
        x += 1

    inner()
    print(x)  # 11
```

### Variable Shadowing

```python
x = "global"

def shadow_example():
    x = "local"  # This shadows the global x
    print(f"Local x: {x}")

    def inner():
        x = "inner"  # This shadows the enclosing x
        print(f"Inner x: {x}")

    inner()
    print(f"Enclosing x: {x}")

shadow_example()
print(f"Global x: {x}")
```

### Best Practices

```python
# 1. Avoid global variables when possible
# 2. Use descriptive variable names to avoid shadowing
# 3. Be explicit with global/nonlocal when needed
# 4. Understand LEGB order before writing complex nested functions

# Good practice: Pass parameters instead of using global
def process_data(data, config=None):
    if config is None:
        config = get_default_config()  # Function call instead of global
    # Process data...

# Good practice: Use class attributes instead of module globals
class DataProcessor:
    default_config = {"setting": "value"}

    def process(self, data):
        config = getattr(self, 'config', self.default_config)
        # Process with config...
```

## Notes

- **LEGB Rule**: Local → Enclosing → Global → Built-in (search order)
- Variables are resolved at runtime, not compile time
- Assignment creates a local variable (unless declared global/nonlocal)
- Functions create their own local scope
- Classes create a new local scope for their methods
- Avoid modifying variables from outer scopes when possible
- Use `global` sparingly and `nonlocal` for nested functions
- Variable shadowing can lead to confusing bugs
- Built-in names can be shadowed (avoid this)
