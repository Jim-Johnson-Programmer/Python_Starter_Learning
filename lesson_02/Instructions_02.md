# Lesson 02: Python Variable Naming Rules

## Variable Naming Rules in Python

[Dave talks about variable naming rules in Python](https://youtu.be/qwAFL1597eM?t=1186)

When creating variables in Python, it's important to follow certain naming rules and conventions to ensure your code is readable and functions correctly. Below are the key rules and best practices for naming variables in Python.

### 1. Basic Rules (Required)

- Variable names must start with a letter (a-z, A-Z) or underscore (\_)
- Variable names cannot start with a number
- Variable names can only contain letters, numbers, and underscores
- Variable names are case-sensitive (`age` and `Age` are different variables)
- Variable names cannot be Python keywords (reserved words)

### 2. Python Keywords (Cannot be used as variable names)

```
and, as, assert, break, class, continue, def, del, elif, else, except,
False, finally, for, from, global, if, import, in, is, lambda, None,
nonlocal, not, or, pass, raise, return, True, try, while, with, yield
```

### 3. Naming Conventions (Best Practices)

#### Snake Case (Recommended for Python)

- Use lowercase letters with underscores to separate words
- Examples:
  ```python
  first_name = "John"
  student_age = 15
  total_score = 95
  is_enrolled = True
  ```

#### Descriptive Names

- Use meaningful names that describe the variable's purpose
- **Good examples:**
  ```python
  username = "praneel123"
  temperature_celsius = 25.5
  number_of_students = 30
  ```
- **Poor examples:**
  ```python
  x = "praneel123"     # Not descriptive
  temp = 25.5          # Ambiguous abbreviation
  n = 30               # Single letter, unclear meaning
  ```

#### Constants

- Use ALL_CAPS with underscores for constants
- Examples:
  ```python
  PI = 3.14159
  MAX_STUDENTS = 50
  DEFAULT_TIMEOUT = 30
  ```

### 4. Valid vs Invalid Examples

#### ✅ Valid Variable Names

```python
name = "Alice"
_private_var = 42
age2 = 16
first_name = "Bob"
PI = 3.14159
isActive = True  # CamelCase (less common in Python)
```

#### ❌ Invalid Variable Names

```python
2name = "Alice"      # Cannot start with number
first-name = "Bob"   # Hyphens not allowed
class = "Math"       # 'class' is a keyword
first name = "Carol" # Spaces not allowed
@username = "test"   # Special characters not allowed
```

### 5. Special Cases

#### Private Variables

- Use single underscore prefix for internal use inside a module or class
- Example: `_internal_counter = 0`

#### Protected Variables

- Use double underscore prefix for name mangling
- Example: `__private_data = "secret"`

#### Temporary Variables

- Single letters are acceptable for short loops or temporary use
- Examples:

  ```python
  for i in range(10):    # 'i' for loop counter
      print(i)

  for x, y in coordinates:  # 'x' and 'y' for coordinates
      plot_point(x, y)
  ```

### 6. Tips for Good Variable Names

1. **Be descriptive:** `student_count` instead of `sc`
2. **Use full words:** `temperature` instead of `temp`
3. **Be consistent:** If you use `user_name` in one place, don't use `username` elsewhere
4. **Avoid confusion:** Don't use `l` (lowercase L), `O` (uppercase O), or `I` (uppercase i) as single-letter variables
5. **Use boolean naming:** For True/False values, use names like `is_active`, `has_permission`, `can_edit`

### 7. Examples in Context

```python
# Student information
student_name = "Praneel"
student_age = 16
is_enrolled = True
gpa = 3.85

# Course details
course_name = "Python Programming"
total_lessons = 23
current_lesson = 2

# Constants
MAX_ATTEMPTS = 3
PASSING_GRADE = 70
```

Remember: Good variable names make your code easier to read, understand, and maintain!

## Comments in Python

[Dave talks about comments in Python](https://youtu.be/qwAFL1597eM?t=1369)

- Single-line comments start with `#` <br> `# This is a comment`
- Multi-line comments can be created using triple quotes `'''` or `"""`
  ```python
  '''
  This is a multi-line comment.
  It can span multiple lines.
  '''
  ```
- Comments are ignored by the Python interpreter and are used to explain code functionality or provide context.

## Settings to check for format on save in VS Code

[Dave talks about format on save settings in VS Code](https://youtu.be/qwAFL1597eM?t=1534)
UPDATED STEPS TO CHECK FORMAT ON SAVE SETTINGS IN VS CODE:

1. Open VS Code settings (File > Preferences > Settings).
2. Search for "format on save".
3. Ensure the checkbox for "Editor: Format On Save" is checked.
4. Also check that "Format on save mode" dropdown is set to "file".

# Lesson 02 Exercise: Update settings for format on save and format on type.

[Dave talk about format on type settings in VS Code](https://youtu.be/qwAFL1597eM?t=1755)

1. Open VS Code settings (File > Preferences > Settings).
2. Search for "format on save".
3. Ensure the checkbox for "Editor: Format On Save" is checked.
4. Search for "format on type".
5. Ensure the checkbox for "Editor: Format On Type" is checked.
