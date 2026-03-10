# 33-keyword-arguments
# Python learning exercise: Keyword Arguments

"""
WHAT ARE KEYWORD ARGUMENTS?
==========================

Keyword arguments are a way to pass values to functions by explicitly naming the parameters.
Instead of relying on the order of arguments (positional arguments), you can specify which
parameter gets which value by using the parameter name.

WHY USE KEYWORD ARGUMENTS?
=========================
1. Makes code more readable - you can see what each value represents
2. Allows arguments in any order - no need to remember parameter positions
3. Can skip optional parameters and use defaults
4. Self-documenting code - function calls explain themselves

SYNTAX:
=======
function_name(parameter_name=value, another_param=another_value)

RULES:
=====
- Keyword arguments can be mixed with positional arguments
- Positional arguments MUST come BEFORE keyword arguments
- Once you use a keyword argument, all following arguments must be keywords too
- Keywords make your code more maintainable and less error-prone
"""

def describe_person(name, age, city):
    """
    A simple function that takes three parameters.
    We can call this function in different ways:
    - describe_person("Alice", 25, "NYC")           # positional
    - describe_person(name="Bob", age=30, city="LA") # keyword
    - describe_person("Charlie", age=35, city="SF")  # mixed
    """
    return f"{name} is {age} years old and lives in {city}."

def create_user(username, email, age=18, active=True):
    """
    Function with default arguments (covered in previous lesson).
    Keyword arguments work great with defaults - you can override only what you need.
    """
    status = "active" if active else "inactive"
    return f"User: {username}, Email: {email}, Age: {age}, Status: {status}"

def calculate_total(price, tax_rate=0.08, discount=0.0):
    """
    Real-world example: calculating a total price.
    With keyword arguments, the function call reads like a configuration:
    calculate_total(price=100, tax_rate=0.10, discount=0.05)
    Much clearer than: calculate_total(100, 0.10, 0.05)
    """
    subtotal = price * (1 - discount)
    tax = subtotal * tax_rate
    total = subtotal + tax
    return f"Total: ${total:.2f} (Price: ${price:.2f}, Tax: ${tax:.2f}, Discount: {discount*100:.0f}%)"

def send_message(recipient, message, priority="normal", sender="System"):
    """
    Another real-world example: sending messages.
    Keyword arguments make it easy to set only the parameters you care about.
    """
    return f"From: {sender}\nTo: {recipient}\nPriority: {priority}\nMessage: {message}"

def main():
    print("=== Keyword Arguments Exercise ===\n")

    # Example 1: Basic keyword arguments
    print("1. Basic Keyword Arguments:")
    print("Positional:", describe_person("Alice", 25, "New York"))
    #           name="Alice", age=25, city="New York" (but order matters)

    print("Keywords (different order):", describe_person(age=30, name="Bob", city="London"))
    #           With keywords, order doesn't matter! age=30, name="Bob", city="London"

    print("Mixed:", describe_person("Charlie", age=35, city="Paris"))
    #           First positional ("Charlie"), then keywords (age=35, city="Paris")
    print()

    # Example 2: With default arguments
    print("2. Keyword Arguments with Defaults:")
    print(create_user("john_doe", "john@example.com"))  # Uses all defaults (age=18, active=True)
    print(create_user("jane_doe", "jane@example.com", age=25))  # Override only age
    print(create_user("mike_smith", "mike@example.com", active=False))  # Override only active status
    print(create_user(username="sarah_jones", email="sarah@example.com", age=28, active=True))  # All keywords
    print()

    # Example 3: Real-world calculation example
    print("3. Calculation with Keyword Arguments:")
    print(calculate_total(100))  # Basic price, uses defaults (tax_rate=0.08, discount=0.0)
    print(calculate_total(100, tax_rate=0.10))  # Override tax rate only
    print(calculate_total(price=200, discount=0.15, tax_rate=0.05))  # All keywords, any order!
    print()

    # Example 4: Message sending simulation
    print("4. Message Sending Example:")
    print(send_message("user1", "Hello there!"))  # Uses defaults for priority and sender
    print(send_message(message="Urgent: System maintenance", recipient="admin", priority="high", sender="Alert System"))
    #           All keywords, in any order - very readable!
    print()

    # Example 5: Demonstrating flexibility
    print("5. Argument Order Flexibility:")
    # All these calls produce the same result but with different argument styles
    result1 = describe_person("David", 40, "Tokyo")  # All positional - must be in order: name, age, city
    result2 = describe_person("David", age=40, city="Tokyo")  # Mixed: positional name, keyword age and city
    result3 = describe_person(name="David", age=40, city="Tokyo")  # All keywords - order doesn't matter
    result4 = describe_person(city="Tokyo", name="David", age=40)  # Keywords in different order - still works!

    print(f"All positional: {result1}")
    print(f"Mixed: {result2}")
    print(f"All keywords: {result3}")
    print(f"Keywords reordered: {result4}")
    print(f"All results are identical: {result1 == result2 == result3 == result4}")

if __name__ == "__main__":
    main()
