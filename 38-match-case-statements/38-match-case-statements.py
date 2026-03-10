# 38-match-case-statements
# Python learning exercise: Understanding match-case statements

def main():
    print("=== Match-Case Statements in Python ===\n")

    # Basic Match-Case Syntax
    print("1. Basic Match-Case Syntax:")

    def check_value(x):
        match x:
            case 1:
                return "one"
            case 2:
                return "two"
            case 3:
                return "three"
            case _:
                return "other"

    for i in [1, 2, 3, 4]:
        print(f"check_value({i}) = {check_value(i)}")
    print()

    # Literal Patterns
    print("2. Literal Patterns:")

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

    print(f"describe_number(1) = {describe_number(1)}")
    print(f"describe_number(5) = {describe_number(5)}")
    print()

    # Variable Patterns (Capture)
    print("3. Variable Patterns (Capture):")

    def process_data(data):
        match data:
            case {"type": "user", "name": name, "age": age}:
                return f"User {name} is {age} years old"
            case {"type": "product", "name": name, "price": price}:
                return f"Product {name} costs ${price}"
            case _:
                return "Unknown data type"

    user_data = {"type": "user", "name": "Alice", "age": 30}
    product_data = {"type": "product", "name": "Laptop", "price": 999}
    unknown_data = {"type": "unknown"}

    print(f"process_data(user_data) = {process_data(user_data)}")
    print(f"process_data(product_data) = {process_data(product_data)}")
    print(f"process_data(unknown_data) = {process_data(unknown_data)}")
    print()

    # OR Patterns
    print("4. OR Patterns:")

    def get_day_type(day):
        match day:
            case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
                return "Weekday"
            case "Saturday" | "Sunday":
                return "Weekend"
            case _:
                return "Invalid day"

    days = ["Monday", "Saturday", "Sunday", "InvalidDay"]
    for day in days:
        print(f"get_day_type('{day}') = {get_day_type(day)}")
    print()

    # Guard Conditions
    print("5. Guard Conditions:")

    def categorize_number(n):
        match n:
            case str():
                return "not a number"
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

    numbers = [-5, 0, 5, 15, "not_a_number"]
    for num in numbers:
        print(f"categorize_number({num}) = {categorize_number(num)}")
    print()

    # Sequence Patterns
    print("6. Sequence Patterns:")

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

    test_lists = [[], [1], [1, 2], [1, 2, 3, 4, 5], "not_a_list"]
    for lst in test_lists:
        print(f"analyze_list({lst}) = {analyze_list(lst)}")
    print()

    # Sequence Patterns with Specific Values
    print("7. Sequence Patterns with Specific Values:")

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

    sequences = [[1, 2, 3], [1, 4, 6, 10], [2, 3, 4, 5], [1, 2, 4]]
    for seq in sequences:
        print(f"check_sequence({seq}) = {check_sequence(seq)}")
    print()

    # Mapping Patterns
    print("8. Mapping Patterns:")

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

    configs = [
        {"database": {"host": "localhost", "port": 5432}, "debug": True},
        {"database": {"host": "prod-db.example.com", "port": 5432}},
        {"api_key": "secret123", "timeout": 30}
    ]

    for config in configs:
        print(f"process_config({config}) = {process_config(config)}")
    print()

    # Class Patterns
    print("9. Class Patterns:")

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

    points = [Point(0, 0), Point(0, 5), Point(3, 0), Point(2, 3), "not_a_point"]
    for point in points:
        print(f"describe_point({point}) = {describe_point(point)}")
    print()

    # Nested Patterns
    print("10. Nested Patterns:")

    def analyze_nested(data):
        match data:
            case {"users": [{"name": name, "active": True}, *rest]}:
                return f"First active user: {name}"
            case {"products": products} if products and products[-1].get("category") == "electronics":
                price = products[-1].get("price")
                return f"Last electronics product costs ${price}"
            case [x, [y, z]]:
                return f"Nested list: {x} contains [{y}, {z}]"
            case _:
                return "No match found"

    nested_data = [
        {"users": [{"name": "Alice", "active": True}, {"name": "Bob", "active": False}]},
        {"products": [{"category": "books"}, {"category": "electronics", "price": 299}]},
        [1, [2, 3]],
        "no_match"
    ]

    for data in nested_data:
        print(f"analyze_nested({data}) = {analyze_nested(data)}")
    print()

    # Practical Examples
    print("11. Practical Examples:")

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

    status_codes = [200, 201, 404, 500, 999]
    for code in status_codes:
        print(f"handle_http_status({code}) = {handle_http_status(code)}")

    print()

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

    commands = ["help", "run script.py", "run script.py --debug", "unknown command"]
    for cmd in commands:
        print(f"parse_command('{cmd}') = {parse_command(cmd)}")

    print("\n=== End of Match-Case Statements Demo ===")

if __name__ == "__main__":
    main()
