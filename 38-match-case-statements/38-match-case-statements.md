# 38-match-case-statements

## Overview

Match-case statements (introduced in Python 3.10) provide a powerful pattern matching mechanism that goes beyond simple if-elif chains. They allow you to match values against patterns and execute code based on the match. This feature is inspired by pattern matching in functional programming languages and provides a more expressive and readable way to handle complex conditional logic.

## Learning Objectives

- Understand the basic syntax of match-case statements
- Learn different types of patterns (literal, variable, wildcard, OR, sequence, mapping)
- Explore guard conditions for additional filtering
- Practice using match-case with different data types
- Compare match-case with traditional if-elif chains
- Understand when to use match-case vs other control structures

## Code Examples

### Basic Match-Case Syntax

```python
# Traditional if-elif approach
def check_value(x):
    if x == 1:
        return "one"
    elif x == 2:
        return "two"
    elif x == 3:
        return "three"
    else:
        return "other"

# Match-case approach
def check_value_match(x):
    match x:
        case 1:
            return "one"
        case 2:
            return "two"
        case 3:
            return "three"
        case _:
            return "other"
```

### Literal Patterns

```python
def describe_number(n):
    match n:
        case 0:
            return "zero"
        case 1:
            return "one"
        case 2:
            return "two"
        case _:
            return f"number: {n}"

print(describe_number(1))  # "one"
print(describe_number(5))  # "number: 5"
```

### Variable Patterns (Capture)

```python
def process_data(data):
    match data:
        case {"type": "user", "name": name, "age": age}:
            return f"User {name} is {age} years old"
        case {"type": "product", "name": name, "price": price}:
            return f"Product {name} costs ${price}"
        case _:
            return "Unknown data type"

user_data = {"type": "user", "name": "Alice", "age": 30}
print(process_data(user_data))  # "User Alice is 30 years old"
```

### OR Patterns

```python
def get_day_type(day):
    match day:
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return "Weekday"
        case "Saturday" | "Sunday":
            return "Weekend"
        case _:
            return "Invalid day"

print(get_day_type("Monday"))  # "Weekday"
print(get_day_type("Saturday"))  # "Weekend"
```

### Guard Conditions

```python
def categorize_number(n):
    match n:
        case x if x < 0:
            return "negative"
        case x if x == 0:
            return "zero"
        case x if x > 0 and x < 10:
            return "small positive"
        case x if x >= 10:
            return "large positive"
        case _:
            return "not a number"

print(categorize_number(-5))   # "negative"
print(categorize_number(5))    # "small positive"
print(categorize_number(15))   # "large positive"
```

### Sequence Patterns

```python
def analyze_list(data):
    match data:
        case []:
            return "Empty list"
        case [x]:
            return f"Single element: {x}"
        case [x, y]:
            return f"Two elements: {x}, {y}"
        case [x, y, *rest]:
            return f"Multiple elements: {x}, {y}, and {len(rest)} more"
        case _:
            return "Not a list"

print(analyze_list([]))              # "Empty list"
print(analyze_list([1]))             # "Single element: 1"
print(analyze_list([1, 2]))          # "Two elements: 1, 2"
print(analyze_list([1, 2, 3, 4, 5])) # "Multiple elements: 1, 2, and 3 more"
```

### Sequence Patterns with Specific Values

```python
def check_sequence(seq):
    match seq:
        case [1, 2, 3]:
            return "Exact match: [1, 2, 3]"
        case [1, *middle, 10]:
            return f"Starts with 1, ends with 10, middle: {middle}"
        case [*head, 5]:
            return f"Ends with 5, head: {head}"
        case _:
            return "No match"

print(check_sequence([1, 2, 3]))      # "Exact match: [1, 2, 3]"
print(check_sequence([1, 4, 6, 10]))   # "Starts with 1, ends with 10, middle: [4, 6]"
print(check_sequence([2, 3, 4, 5]))    # "Ends with 5, head: [2, 3, 4]"
```

### Mapping Patterns

```python
def process_config(config):
    match config:
        case {"database": {"host": host, "port": port}, "debug": True}:
            return f"Debug mode: connecting to {host}:{port}"
        case {"database": {"host": host, "port": port}}:
            return f"Production mode: connecting to {host}:{port}"
        case {"api_key": key, **rest}:
            return f"API key found, other config: {rest}"
        case _:
            return "Invalid configuration"

config1 = {"database": {"host": "localhost", "port": 5432}, "debug": True}
print(process_config(config1))  # "Debug mode: connecting to localhost:5432"
```

### Class Patterns

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def describe_point(point):
    match point:
        case Point(x=0, y=0):
            return "Origin"
        case Point(x=0, y=y):
            return f"On Y-axis at y={y}"
        case Point(x=x, y=0):
            return f"On X-axis at x={x}"
        case Point(x=x, y=y):
            return f"Point at ({x}, {y})"
        case _:
            return "Not a point"

p1 = Point(0, 0)
p2 = Point(0, 5)
p3 = Point(3, 0)
p4 = Point(2, 3)

print(describe_point(p1))  # "Origin"
print(describe_point(p2))  # "On Y-axis at y=5"
print(describe_point(p3))  # "On X-axis at x=3"
print(describe_point(p4))  # "Point at (2, 3)"
```

### Nested Patterns

```python
def analyze_nested(data):
    match data:
        case {"users": [{"name": name, "active": True}, *rest]}:
            return f"First active user: {name}"
        case {"products": [*, {"category": "electronics", "price": price}]}:
            return f"Last electronics product costs ${price}"
        case [x, [y, z]]:
            return f"Nested list: {x} contains [{y}, {z}]"
        case _:
            return "No match found"

data1 = {"users": [{"name": "Alice", "active": True}, {"name": "Bob", "active": False}]}
print(analyze_nested(data1))  # "First active user: Alice"

data2 = [1, [2, 3]]
print(analyze_nested(data2))  # "Nested list: 1 contains [2, 3]"
```

### Practical Examples

```python
# HTTP Status Code Handler
def handle_http_status(status_code):
    match status_code:
        case 200:
            return "OK"
        case 201:
            return "Created"
        case 400:
            return "Bad Request"
        case 401:
            return "Unauthorized"
        case 403:
            return "Forbidden"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return f"Unknown status: {status_code}"

# Command Line Argument Parser
def parse_command(command):
    match command.split():
        case ["help" | "-h" | "--help"]:
            return "Show help"
        case ["version" | "-v" | "--version"]:
            return "Show version"
        case ["run", filename]:
            return f"Run file: {filename}"
        case ["run", filename, "--debug"]:
            return f"Run file in debug mode: {filename}"
        case _:
            return "Unknown command"

print(parse_command("run script.py"))        # "Run file: script.py"
print(parse_command("run script.py --debug")) # "Run file in debug mode: script.py"
print(parse_command("help"))                 # "Show help"
```

## Notes

- Match-case statements require Python 3.10 or later
- The `case _:` pattern acts as a wildcard (like `else` in if-elif)
- Patterns are evaluated in order from top to bottom
- Only the first matching pattern executes
- Variable patterns capture values for use in the case block
- Guard conditions (`if`) add additional constraints to patterns
- Sequence patterns use `*` for variable-length sequences
- Mapping patterns can use `**` to capture remaining key-value pairs
- Class patterns work with both positional and keyword arguments
- Match-case can often replace complex if-elif chains more readably
- Use match-case when you have many specific cases to handle, especially with structured data
