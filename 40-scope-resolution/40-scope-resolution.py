# 40-scope-resolution
# Python learning exercise: Understanding scope resolution

# Global variables for demonstration
counter = 0
global_x = 10

def increment_counter():
    """Function to demonstrate global scope"""
    global counter
    counter += 1
    print(f"  Counter: {counter}")

def main():
    print("=== Python Scope Resolution Tutorial ===\n")

    # 1. LEGB Rule Overview
    print("1. LEGB Rule Overview:")
    # Built-in scope (B) - Available everywhere
    print(f"Built-in len('hello'): {len('hello')}")

    # Global scope (G) - Module level variables
    global_var = "I'm global"

    def outer_function():
        # Enclosing scope (E) - Variables in outer functions
        enclosing_var = "I'm enclosing"

        def inner_function():
            # Local scope (L) - Variables defined in current function
            local_var = "I'm local"

            print(f"  Local scope: {local_var}")
            print(f"  Enclosing scope: {enclosing_var}")
            print(f"  Global scope: {global_var}")
            print(f"  Built-in scope len('test'): {len('test')}")

        inner_function()

    outer_function()
    print()

    # 2. Local Scope
    print("2. Local Scope:")
    def local_scope_example():
        x = 10  # Local variable
        print(f"  Inside function: x = {x}")

    x = 5  # Global variable
    local_scope_example()
    print(f"  Outside function: x = {x}")
    print()

    # 3. Enclosing Scope (Nested Functions)
    print("3. Enclosing Scope (Nested Functions):")
    def outer():
        x = "outer"

        def inner():
            x = "inner"
            print(f"  Inner function: x = {x}")

        inner()
        print(f"  Outer function: x = {x}")

    outer()
    print()

    # 4. Global Scope
    print("4. Global Scope:")

    increment_counter()
    increment_counter()
    print(f"  Global counter: {counter}")
    print()

    # 5. Built-in Scope
    print("5. Built-in Scope:")
    # Use built-in functions explicitly
    import builtins
    print(f"  Built-in max([1, 2, 3]): {builtins.max([1, 2, 3])}")
    print(f"  Built-in min([1, 2, 3]): {builtins.min([1, 2, 3])}")

    # Shadowing built-in (demonstration - don't do this in real code)
    def max(a, b):  # This shadows built-in max
        return a if a > b else b

    print(f"  Our max(5, 10): {max(5, 10)}")
    print()

    # 6. The global Keyword
    print("6. The global Keyword:")
    x = 10

    def modify_global():
        global x
        x = 20

    def try_modify_global():
        global x
        x = 30

    print(f"  Initial x: {x}")
    modify_global()
    print(f"  After modify_global: {x}")
    try_modify_global()
    print(f"  After try_modify_global: {x}")
    print()

    # 7. The nonlocal Keyword
    print("7. The nonlocal Keyword:")
    def outer_nonlocal():
        x = "outer"

        def middle():
            x = "middle"

            def inner():
                nonlocal x
                x = "modified by inner"

            print(f"  Before inner: x = {x}")
            inner()
            print(f"  After inner: x = {x}")

        middle()
        print(f"  Outer x: {x}")

    outer_nonlocal()
    print()

    # 8. Scope Resolution Order
    print("8. Scope Resolution Order:")
    x = "global"

    def outer_resolution():
        x = "enclosing"

        def inner():
            x = "local"
            print(f"  Local x: {x}")

            def innermost():
                print(f"  Enclosing x (from innermost): {x}")

            innermost()

        inner()

    outer_resolution()
    print()

    # 9. Classes and Scope
    print("9. Classes and Scope:")
    class ScopeExample:
        class_var = "class variable"

        def __init__(self):
            self.instance_var = "instance variable"

        def method(self):
            local_var = "local variable"
            print(f"  Local: {local_var}")
            print(f"  Instance: {self.instance_var}")
            print(f"  Class: {self.class_var}")
            print(f"  Global x: {globals().get('x', 'not found')}")

    obj = ScopeExample()
    obj.method()
    print()

    # 10. Common Scope Errors and Solutions
    print("10. Common Scope Errors and Solutions:")

    # Error 1: UnboundLocalError (commented out to avoid error)
    # x = 10
    # def problematic():
    #     print(x)  # This would work
    #     x = 20    # But this makes x local, causing UnboundLocalError

    # Solution: Use global keyword
    def correct():
        global x
        print(f"  In correct(): x = {x}")
        x = 40

    print(f"  Before correct(): x = {x}")
    correct()
    print(f"  After correct(): x = {x}")
    print()

    # Error 2: Modifying enclosing variable
    def outer_fixed():
        x = 50

        def inner():
            nonlocal x
            x += 1

        print(f"  Before inner(): x = {x}")
        inner()
        print(f"  After inner(): x = {x}")

    outer_fixed()
    print()

    # 11. Variable Shadowing
    print("11. Variable Shadowing:")
    x = "global"

    def shadow_example():
        x = "local"
        print(f"  Local x: {x}")

        def inner():
            x = "inner"
            print(f"  Inner x: {x}")

        inner()
        print(f"  Enclosing x: {x}")

    shadow_example()
    print(f"  Global x: {x}")
    print()

    # 12. Best Practices Demonstration
    print("12. Best Practices:")

    # Good: Pass parameters instead of using global
    def process_data_good(data, config=None):
        if config is None:
            config = {"setting": "default"}
        return f"Processing {data} with {config}"

    print(f"  Good practice: {process_data_good('data1')}")
    print(f"  Good practice with config: {process_data_good('data2', {'setting': 'custom'})}")

    # Good: Use class attributes
    class DataProcessor:
        default_config = {"setting": "class_default"}

        def process(self, data):
            config = getattr(self, 'config', self.default_config)
            return f"Processing {data} with {config}"

    processor = DataProcessor()
    print(f"  Class attribute: {processor.process('data3')}")

    processor.config = {"setting": "instance_config"}
    print(f"  Instance attribute: {processor.process('data4')}")
    print()

    # 13. LEGB Hierarchy Demonstration
    print("13. LEGB Hierarchy Demonstration:")
    builtin_var = "This is not a real builtin, just for demo"

    def demonstrate_legb():
        global_var = "global level"
        print(f"  Global level: {global_var}")

        def enclosing_func():
            enclosing_var = "enclosing level"
            print(f"    Enclosing level: {enclosing_var}")

            def local_func():
                local_var = "local level"
                print(f"      Local level: {local_var}")
                print(f"      Accessing enclosing: {enclosing_var}")
                print(f"      Accessing global: {global_var}")
                print(f"      Accessing builtin-like: {len('builtin demo')}")

            local_func()

        enclosing_func()

    demonstrate_legb()

    print("\n=== End of Scope Resolution Tutorial ===")

if __name__ == "__main__":
    main()
