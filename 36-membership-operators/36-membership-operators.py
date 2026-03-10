# 36-membership-operators
# Python learning exercise: Understanding membership operators

def main():
    print("=== Membership Operators in Python ===\n")

    # Basic Usage with Lists
    print("1. Basic Usage with Lists:")
    fruits = ['apple', 'banana', 'cherry', 'date']

    print(f"'apple' in fruits: {'apple' in fruits}")      # True
    print(f"'grape' in fruits: {'grape' in fruits}")      # False
    print(f"'grape' not in fruits: {'grape' not in fruits}")  # True
    print(f"'apple' not in fruits: {'apple' not in fruits}")  # False
    print()

    # Working with Strings
    print("2. Working with Strings:")
    text = "Hello, World!"

    print(f"'Hello' in text: {'Hello' in text}")        # True
    print(f"'hello' in text: {'hello' in text}")        # False (case-sensitive)
    print(f"'World' in text: {'World' in text}")        # True
    print(f"'Python' in text: {'Python' in text}")       # False
    print(f"'Python' not in text: {'Python' not in text}")   # True
    print()

    # Using with Tuples
    print("3. Using with Tuples:")
    coordinates = (10, 20, 30, 40)

    print(f"20 in coordinates: {20 in coordinates}")      # True
    print(f"50 in coordinates: {50 in coordinates}")      # False
    print(f"50 not in coordinates: {50 not in coordinates}")  # True
    print()

    # Working with Sets
    print("4. Working with Sets:")
    numbers = {1, 2, 3, 4, 5}

    print(f"3 in numbers: {3 in numbers}")           # True
    print(f"6 in numbers: {6 in numbers}")           # False

    # Sets are very fast for membership testing
    large_set = set(range(1000))  # Smaller for demo, but still fast
    print(f"999 in large_set: {999 in large_set}")     # True (very fast operation)
    print()

    # Dictionary Membership Testing
    print("5. Dictionary Membership Testing:")
    student_grades = {'Alice': 95, 'Bob': 87, 'Charlie': 92}

    print(f"'Alice' in student_grades: {'Alice' in student_grades}")      # True
    print(f"'David' in student_grades: {'David' in student_grades}")      # False

    # To check values, use .values()
    print(f"95 in student_grades.values(): {95 in student_grades.values()}")  # True
    print(f"100 in student_grades.values(): {100 in student_grades.values()}") # False
    print()

    # Using in Conditional Statements
    print("6. Using in Conditional Statements:")

    def check_vowel(char):
        vowels = 'aeiouAEIOU'
        if char in vowels:
            return f"'{char}' is a vowel"
        else:
            return f"'{char}' is not a vowel"

    print(f"check_vowel('a'): {check_vowel('a')}")  # 'a' is a vowel
    print(f"check_vowel('b'): {check_vowel('b')}")  # 'b' is not a vowel

    def categorize_character(char):
        if char in 'aeiouAEIOU':
            return "Vowel"
        elif char in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            return "Consonant"
        elif char in '0123456789':
            return "Digit"
        else:
            return "Special character"

    print(f"categorize_character('A'): {categorize_character('A')}")  # Vowel
    print(f"categorize_character('3'): {categorize_character('3')}")  # Digit
    print(f"categorize_character('@'): {categorize_character('@')}")  # Special character
    print()

    # Practical Examples
    print("7. Practical Examples:")

    # Checking user permissions
    user_roles = ['admin', 'editor', 'viewer']

    def has_access(user_role, required_role):
        return user_role in user_roles and (user_role == required_role or user_role == 'admin')

    print(f"has_access('admin', 'editor'): {has_access('admin', 'editor')}")  # True (admin has all access)
    print(f"has_access('viewer', 'editor'): {has_access('viewer', 'editor')}") # False

    # Filtering data
    data = [10, 20, 30, 40, 50]
    allowed_values = [20, 30, 40]

    filtered_data = [x for x in data if x in allowed_values]
    print(f"Filtered data: {filtered_data}")  # [20, 30, 40]

    # Checking for forbidden items
    shopping_cart = ['apple', 'banana', 'cherry']
    forbidden_items = ['cherry', 'date']

    has_forbidden = any(item in forbidden_items for item in shopping_cart)
    print(f"Cart has forbidden items: {has_forbidden}")  # True

    print("\n=== End of Membership Operators Demo ===")

if __name__ == "__main__":
    main()
