# 34-star-args-dbl-star-kwargs
# Python learning exercise: *args and **kwargs

"""
WHAT ARE *args AND **kwargs?
============================

*args and **kwargs are special syntax in Python that allow functions to accept a variable
number of arguments. They're incredibly useful for creating flexible functions.

*args (star args):
- Allows a function to accept any number of positional arguments
- Arguments are collected into a tuple
- The name 'args' is conventional - you can use any name after *

**kwargs (double star kwargs):
- Allows a function to accept any number of keyword arguments
- Arguments are collected into a dictionary
- The name 'kwargs' is conventional - you can use any name after **

WHY USE THEM?
============
- Create flexible APIs that can handle different numbers of arguments
- Build wrapper functions that pass arguments to other functions
- Handle configuration options dynamically
- Make functions more future-proof

SYNTAX RULES:
============
- *args must come before **kwargs in function definitions
- In function calls, positional args come before keyword args
- You can use different names (*numbers, **settings) but args/kwargs are conventional
"""

def sum_all(*args):
    """Sum any number of numbers using *args."""
    print(f"Received {len(args)} arguments: {args}")
    return sum(args)

def print_person_info(**kwargs):
    """Print person information using **kwargs."""
    print("Person Information:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

def flexible_greeting(*args, **kwargs):
    """A greeting function that accepts both types of arguments."""
    greeting = kwargs.get('greeting', 'Hello')
    separator = kwargs.get('separator', ' ')

    if args:
        names = separator.join(str(arg) for arg in args)
        print(f"{greeting}, {names}!")
    else:
        print(f"{greeting}!")

def calculate_total(price, tax_rate=0.08, *discounts, **extra_fees):
    """
    Calculate total with variable discounts and fees.
    - price: required positional argument
    - tax_rate: keyword argument with default
    - *discounts: variable positional arguments (discount percentages)
    - **extra_fees: variable keyword arguments (like shipping=5.99, handling=2.50)
    """
    # Apply discounts
    total_discount = 0
    for discount in discounts:
        total_discount += price * (discount / 100)

    subtotal = price - total_discount

    # Apply tax
    tax = subtotal * tax_rate

    # Add extra fees
    total_fees = sum(extra_fees.values())

    final_total = subtotal + tax + total_fees

    print(f"Price: ${price:.2f}")
    print(f"Discounts applied: {list(discounts)}")
    print(f"Subtotal after discounts: ${subtotal:.2f}")
    print(f"Tax ({tax_rate*100:.0f}%): ${tax:.2f}")
    print(f"Extra fees: {extra_fees}")
    print(f"Final total: ${final_total:.2f}")
    return final_total

def demonstrate_unpacking():
    """Demonstrate argument unpacking with * and **."""

    def simple_add(a, b, c):
        return a + b + c

    def display_info(name, age, city, profession=None):
        info = f"{name} is {age} years old, lives in {city}"
        if profession:
            info += f", and works as a {profession}"
        return info + "."

    # Unpacking a list/tuple with *
    numbers = [1, 2, 3]
    print(f"simple_add(*numbers): {simple_add(*numbers)}")

    # Unpacking a dictionary with **
    person_data = {"name": "Alice", "age": 30, "city": "Boston", "profession": "Engineer"}
    print(f"display_info(**person_data): {display_info(**person_data)}")

    # Partial unpacking
    basic_info = {"name": "Bob", "age": 25, "city": "Seattle"}
    print(f"display_info(**basic_info): {display_info(**basic_info)}")

def main():
    print("=== *args and **kwargs Exercise ===\n")

    # Example 1: Basic *args
    print("1. Basic *args - Variable Positional Arguments:")
    print(f"sum_all(1, 2, 3): {sum_all(1, 2, 3)}")
    print(f"sum_all(10, 20, 30, 40, 50): {sum_all(10, 20, 30, 40, 50)}")
    print(f"sum_all(): {sum_all()}")  # No arguments
    print()

    # Example 2: Basic **kwargs
    print("2. Basic **kwargs - Variable Keyword Arguments:")
    print_person_info(name="Alice", age=25, city="New York", profession="Developer")
    print()
    print_person_info(name="Bob", hobby="Photography", favorite_food="Pizza")
    print()

    # Example 3: Using both *args and **kwargs
    print("3. Using Both *args and **kwargs:")
    flexible_greeting("Alice", "Bob", "Charlie", greeting="Good morning", separator=", ")
    flexible_greeting(greeting="Hi there")
    flexible_greeting("David", greeting="Welcome", separator=" and ")
    print()

    # Example 4: Real-world example with both
    print("4. Real-World Example - Shopping Cart Total:")
    calculate_total(100, tax_rate=0.08, shipping=9.99, handling=2.50)  # price=100, default tax, fees
    print()
    calculate_total(50, tax_rate=0.10, processing=1.99)  # Different tax rate, one fee
    print()
    calculate_total(150, 15, shipping=12.99, insurance=8.50)  # price=150, tax_rate=15 (overriding default), fees
    print()

    # Example 5: Argument unpacking
    print("5. Argument Unpacking:")
    demonstrate_unpacking()
    print()

    # Example 6: Common patterns
    print("6. Common Patterns and Best Practices:")

    # Pattern 1: Wrapper function
    def my_print(*args, **kwargs):
        print("Custom print function:")
        print(*args, **kwargs)  # Pass all arguments to built-in print

    my_print("Hello", "world", sep="-", end="!\n")
    print()

    # Pattern 2: Function that accepts any arguments
    def logger(*args, **kwargs):
        """Log any function call."""
        print(f"Function called with args: {args}, kwargs: {kwargs}")

    logger("some", "arguments", action="save", user_id=123)
    print()

    # Pattern 3: Building flexible APIs
    def create_api_endpoint(method, path, *middleware, **config):
        """Simulate creating an API endpoint."""
        print(f"Creating {method} endpoint at {path}")
        print(f"Middleware: {middleware}")
        print(f"Configuration: {config}")

    create_api_endpoint("POST", "/users", "auth", "validate", cache=True, rate_limit=100)

if __name__ == "__main__":
    main()
