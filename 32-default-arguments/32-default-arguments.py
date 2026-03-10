# 32-default-arguments
# Python learning exercise: Default Arguments

def greet(name, greeting="Hello"):
    """Function with a default argument for greeting."""
    return f"{greeting}, {name}!"

def calculate_area(length, width, unit="square meters"):
    """Calculate area with optional unit specification."""
    area = length * width
    return f"The area is {area} {unit}."

#manadatory arguments must come before default arguments, otherwise it will raise a SyntaxError
def create_profile(name, age=25, city="Unknown"):
    """Create a user profile with default values."""
    return f"Name: {name}, Age: {age}, City: {city}"

def main():
    print("=== Default Arguments Exercise ===\n")

    # Example 1: Basic greeting function
    print("1. Greeting Function:")
    print(greet("Alice", "Hi"))  # Both arguments provided
    print(greet("Bob"))          # Uses default greeting
    print()

    # Example 2: Area calculation
    print("2. Area Calculation:")
    print(calculate_area(5, 10))                    # Uses default unit
    print(calculate_area(5, 10, "square feet"))     # Overrides default
    print()

    # Example 3: User profile
    print("3. User Profile Creation:")
    print(create_profile("John"))                           # All defaults
    print(create_profile("Jane", 30))                       # Override age
    print(create_profile("Mike", city="New York"))          # Override city
    print(create_profile("Sara", 28, "Los Angeles"))        # Override all
    print()

    # Example 4: Demonstrating order matters
    print("4. Default Arguments Order:")
    # This works - defaults come after non-defaults
    def example(a, b=10, c=20):
        return a + b + c

    print(f"example(5): {example(5)}")           # a=5, b=10, c=20
    print(f"example(5, 15): {example(5, 15)}")   # a=5, b=15, c=20
    print(f"example(5, 15, 25): {example(5, 15, 25)}")  # All specified

if __name__ == "__main__":
    main()
