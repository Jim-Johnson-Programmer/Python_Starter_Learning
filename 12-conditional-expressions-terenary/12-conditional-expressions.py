# 12-conditional-expressions
# Python learning exercise

#conditional expressions, also known as ternary operators, 
# allow you to write concise if-else statements in a single line of code. 
# The syntax for a conditional expression is:
# value_if_true if condition else value_if_false

# Example 1: Basic conditional expression
age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult

# Most common use of conditional expressions is to assure that a variable cannot go undefined. 
# For example, if you want to assign a default value to a variable if it is None, 
# you can use a conditional expression like this:
user_input = None
result = user_input if user_input is not None else "Default Value"
print(result)  # Output: Default Value

# This is commonly used by senior developers to assure that a variable is never None, 
# which can help prevent errors in the code.