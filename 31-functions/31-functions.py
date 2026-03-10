# 31-functions
# Python learning exercise

# Function without args
def greet():
    print("Hello, World!")

# Function with args of native types
def add_numbers(a, b):
    print(f"The sum of {a} and {b} is {a + b}")

# Function with returned value
def multiply(x, y):
    return x * y

# Function with in/out args (modifying a mutable argument)
def append_to_list(my_list, item):
    my_list.append(item)
    print(f"List after appending: {my_list}")

# Main demo
if __name__ == "__main__":
    print("Demo of functions without classes:\n")

    # Call function without args
    print("1. Function without arguments:")
    greet()
    print()

    # Call function with args
    print("2. Function with arguments of native types:")
    add_numbers(5, 3)
    add_numbers("Hello", " World")
    print()

    # Call function with returned value
    print("3. Function with returned value:")
    result = multiply(4, 7)
    print(f"4 * 7 = {result}")
    print()

    # Call function with in/out args
    print("4. Function with in/out arguments (modifying a list):")
    my_list = [1, 2, 3]
    print(f"Original list: {my_list}")
    append_to_list(my_list, 4)
    print(f"List after function call: {my_list}")
