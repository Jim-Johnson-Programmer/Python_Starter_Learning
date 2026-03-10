# 37-list-comprehensions
# Python learning exercise: Understanding list comprehensions

def main():
    print("=== List Comprehensions in Python ===\n")

    # Basic List Comprehension
    print("1. Basic List Comprehension:")
    numbers = [1, 2, 3, 4, 5]

    # Traditional for loop approach
    squares_loop = []
    for num in numbers:
        squares_loop.append(num ** 2)
    print(f"Traditional loop: {squares_loop}")

    # List comprehension approach
    squares_comp = [num ** 2 for num in numbers]
    print(f"List comprehension: {squares_comp}")
    print()

    # List Comprehension with Expression
    print("2. List Comprehension with Expression:")
    numbers = [1, 2, 3, 4, 5]
    string_numbers = [str(num) for num in numbers]
    print(f"String conversion: {string_numbers}")

    words = ['hello', 'world', 'python']
    upper_words = [word.upper() for word in words]
    print(f"Uppercase words: {upper_words}")
    print()

    # List Comprehension with Condition (Filtering)
    print("3. List Comprehension with Condition (Filtering):")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = [num for num in numbers if num % 2 == 0]
    print(f"Even numbers: {even_numbers}")

    filtered = [num for num in numbers if num > 3 and num % 2 == 0]
    print(f"Numbers > 3 and even: {filtered}")
    print()

    # List Comprehension with if-else (Conditional Expression)
    print("4. List Comprehension with if-else (Conditional Expression):")
    numbers = [1, 2, 3, 4, 5]
    categories = ['even' if num % 2 == 0 else 'odd' for num in numbers]
    print(f"Number categories: {categories}")

    transformed = [num * 2 if num % 2 == 0 else num for num in numbers]
    print(f"Transformed numbers: {transformed}")
    print()

    # Nested List Comprehensions
    print("5. Nested List Comprehensions:")
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = [num for row in matrix for num in row]
    print(f"Flattened matrix: {flattened}")

    table = [[i * j for j in range(1, 4)] for i in range(1, 4)]
    print("Multiplication table:")
    for row in table:
        print(row)
    print()

    # List Comprehension with Multiple Iterables
    print("6. List Comprehension with Multiple Iterables:")
    names = ['Alice', 'Bob', 'Charlie']
    ages = [25, 30, 35]
    people = [f"{name} is {age} years old" for name, age in zip(names, ages)]
    print("People descriptions:")
    for person in people:
        print(f"  {person}")
    print()

    # Working with Strings
    print("7. Working with Strings:")
    sentence = "The quick brown fox jumps over the lazy dog"
    words = sentence.split()
    long_words = [word for word in words if len(word) > 3]
    print(f"Words longer than 3 chars: {long_words}")

    text = "Hello World"
    vowels = [char for char in text if char.lower() in 'aeiou']
    print(f"Vowels in '{text}': {vowels}")
    print()

    # Dictionary Comprehensions (Related)
    print("8. Dictionary Comprehensions (Related):")
    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    dict_comp = {key: value for key, value in zip(keys, values)}
    print(f"Dictionary from lists: {dict_comp}")

    original = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    filtered_dict = {k: v for k, v in original.items() if v > 2}
    print(f"Filtered dictionary: {filtered_dict}")
    print()

    # Set Comprehensions (Related)
    print("9. Set Comprehensions (Related):")
    numbers = [1, 2, 2, 3, 3, 3, 4]
    unique_squares = {num ** 2 for num in numbers}
    print(f"Unique squares from {numbers}: {unique_squares}")

    numbers_set = {1, 2, 3, 4, 5, 6}
    even_squares = {num ** 2 for num in numbers_set if num % 2 == 0}
    print(f"Even squares from {numbers_set}: {even_squares}")
    print()

    # Practical Examples
    print("10. Practical Examples:")
    data = ["Name,Age,City", "Alice,25,NYC", "Bob,30,LA", "Charlie,35,Chicago"]
    ages = [int(line.split(',')[1]) for line in data[1:]]
    print(f"Ages extracted from CSV-like data: {ages}")

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    diagonal = [matrix[i][i] for i in range(len(matrix))]
    print(f"Diagonal elements: {diagonal}")

    # Performance comparison
    print("\n11. Performance Comparison:")
    import time

    # Large dataset
    large_list = list(range(100000))

    # Traditional loop
    start = time.time()
    squares_loop = []
    for num in large_list:
        squares_loop.append(num ** 2)
    loop_time = time.time() - start

    # List comprehension
    start = time.time()
    squares_comp = [num ** 2 for num in large_list]
    comp_time = time.time() - start

    print(f"Traditional loop time: {loop_time:.4f} seconds")
    print(f"List comprehension time: {comp_time:.4f} seconds")
    print(f"List comprehension is {loop_time/comp_time:.2f}x faster")

    print("\n=== End of List Comprehensions Demo ===")

if __name__ == "__main__":
    main()
