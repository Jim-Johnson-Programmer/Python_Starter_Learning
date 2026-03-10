# 46-oop-python
# Object-Oriented Programming in Python

def main():
    print("=== Object-Oriented Programming Tutorial ===\n")

    # Section 1: Basic Class and Object
    print("1. Basic Class and Object")
    basic_class_demo()
    print()

    # Section 2: Instance Variables vs Class Variables
    print("2. Instance Variables vs Class Variables")
    class_vs_instance_demo()
    print()

    # Section 3: Class Methods and Static Methods
    print("3. Class Methods and Static Methods")
    class_static_methods_demo()
    print()

    # Section 4: Inheritance
    print("4. Inheritance")
    inheritance_demo()
    print()

    # Section 5: Multiple Inheritance
    print("5. Multiple Inheritance")
    multiple_inheritance_demo()
    print()

    # Section 6: Polymorphism
    print("6. Polymorphism")
    polymorphism_demo()
    print()

    # Section 7: Encapsulation with Properties
    print("7. Encapsulation with Properties")
    encapsulation_demo()
    print()

    # Section 8: Magic Methods (Dunder Methods)
    print("8. Magic Methods (Dunder Methods)")
    magic_methods_demo()
    print()

    # Section 9: Abstract Base Classes
    print("9. Abstract Base Classes")
    abstract_classes_demo()
    print()

def basic_class_demo():
    """Demonstrate basic class creation and object instantiation"""
    class Car:
        def __init__(self, make, model, year):
            self.make = make
            self.model = model
            self.year = year

        def start_engine(self):
            return f"The {self.year} {self.make} {self.model}'s engine is starting!"

        def get_description(self):
            return f"{self.year} {self.make} {self.model}"

    # Creating objects (instances)
    car1 = Car("Toyota", "Camry", 2020)
    car2 = Car("Honda", "Civic", 2019)

    print(f"Car 1: {car1.get_description()}")
    print(f"Car 1 engine: {car1.start_engine()}")
    print(f"Car 2: {car2.get_description()}")

def class_vs_instance_demo():
    """Demonstrate class variables vs instance variables"""
    class Employee:
        # Class variable (shared by all instances)
        company_name = "Tech Corp"
        employee_count = 0

        def __init__(self, name, salary):
            # Instance variables (unique to each instance)
            self.name = name
            self.salary = salary
            Employee.employee_count += 1

        def get_info(self):
            return f"{self.name} works at {self.company_name} with salary ${self.salary}"

    # Usage
    emp1 = Employee("Alice", 50000)
    emp2 = Employee("Bob", 60000)

    print(f"Employee 1: {emp1.get_info()}")
    print(f"Employee 2: {emp2.get_info()}")
    print(f"Total employees: {Employee.employee_count}")
    print(f"Company name (class variable): {Employee.company_name}")

def class_static_methods_demo():
    """Demonstrate class methods and static methods"""
    class MathUtils:
        @staticmethod
        def add(a, b):
            """Static method - doesn't need instance or class"""
            return a + b

        @classmethod
        def create_from_string(cls, math_expr):
            """Class method - receives class as first parameter"""
            a, b = map(int, math_expr.split('+'))
            return cls(a, b)

        def __init__(self, a, b):
            self.a = a
            self.b = b

        def multiply(self):
            return self.a * self.b

    # Usage
    result = MathUtils.add(5, 3)  # Static method call
    print(f"Static method result: {result}")

    utils = MathUtils.create_from_string("4+2")  # Class method call
    print(f"Class method result: {utils.multiply()}")

def inheritance_demo():
    """Demonstrate inheritance and method overriding"""
    class Animal:
        def __init__(self, name, species):
            self.name = name
            self.species = species

        def make_sound(self):
            return "Some generic animal sound"

        def get_info(self):
            return f"{self.name} is a {self.species}"

    class Dog(Animal):
        def __init__(self, name, breed):
            super().__init__(name, "Dog")
            self.breed = breed

        def make_sound(self):
            return "Woof!"

        def fetch(self):
            return f"{self.name} is fetching the ball!"

    class Cat(Animal):
        def make_sound(self):
            return "Meow!"

    # Usage
    dog = Dog("Buddy", "Golden Retriever")
    cat = Cat("Whiskers", "Siamese")

    print(f"Dog info: {dog.get_info()}")
    print(f"Dog sound: {dog.make_sound()}")
    print(f"Dog fetch: {dog.fetch()}")

    print(f"Cat info: {cat.get_info()}")
    print(f"Cat sound: {cat.make_sound()}")

def multiple_inheritance_demo():
    """Demonstrate multiple inheritance"""
    class Flyable:
        def fly(self):
            return "Flying high!"

    class Swimmable:
        def swim(self):
            return "Swimming gracefully!"

    class Duck(Flyable, Swimmable):
        def __init__(self, name):
            self.name = name

        def quack(self):
            return "Quack!"

    # Usage
    duck = Duck("Donald")
    print(f"Duck name: {duck.name}")
    print(f"Duck quack: {duck.quack()}")
    print(f"Duck fly: {duck.fly()}")
    print(f"Duck swim: {duck.swim()}")

    # Check method resolution order
    print(f"Method Resolution Order: {Duck.__mro__}")

def polymorphism_demo():
    """Demonstrate polymorphism"""
    class Shape:
        def area(self):
            pass

        def perimeter(self):
            pass

    class Rectangle(Shape):
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def area(self):
            return self.width * self.height

        def perimeter(self):
            return 2 * (self.width + self.height)

    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            return 3.14159 * self.radius ** 2

        def perimeter(self):
            return 2 * 3.14159 * self.radius

    # Polymorphism in action
    shapes = [Rectangle(4, 5), Circle(3), Rectangle(2, 3)]

    print("Shape calculations:")
    for i, shape in enumerate(shapes, 1):
        print(f"Shape {i}: Area = {shape.area():.2f}, Perimeter = {shape.perimeter():.2f}")

def encapsulation_demo():
    """Demonstrate encapsulation with properties"""
    class BankAccount:
        def __init__(self, owner, initial_balance=0):
            self.owner = owner
            self._balance = initial_balance  # Protected attribute

        @property
        def balance(self):
            """Getter for balance"""
            return self._balance

        @balance.setter
        def balance(self, amount):
            """Setter for balance with validation"""
            if amount < 0:
                raise ValueError("Balance cannot be negative")
            self._balance = amount

        def deposit(self, amount):
            if amount > 0:
                self._balance += amount

        def withdraw(self, amount):
            if 0 < amount <= self._balance:
                self._balance -= amount
                return True
            return False

    # Usage
    account = BankAccount("Alice", 1000)
    print(f"Initial balance: ${account.balance}")

    account.deposit(500)
    print(f"After deposit: ${account.balance}")

    success = account.withdraw(200)
    print(f"Withdrawal successful: {success}, Balance: ${account.balance}")

    # Using property setter
    account.balance = 1500
    print(f"After setting balance: ${account.balance}")

    # Try invalid balance
    try:
        account.balance = -100
    except ValueError as e:
        print(f"Error: {e}")

def magic_methods_demo():
    """Demonstrate magic methods (dunder methods)"""
    class Vector:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __str__(self):
            """String representation for print()"""
            return f"Vector({self.x}, {self.y})"

        def __repr__(self):
            """Official string representation"""
            return f"Vector(x={self.x}, y={self.y})"

        def __add__(self, other):
            """Addition operator"""
            return Vector(self.x + other.x, self.y + other.y)

        def __eq__(self, other):
            """Equality comparison"""
            return self.x == other.x and self.y == other.y

        def __len__(self):
            """Length of vector (magnitude)"""
            return int((self.x ** 2 + self.y ** 2) ** 0.5)

    # Usage
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)

    print(f"Vector 1: {v1}")           # Uses __str__
    print(f"Vector 1 repr: {repr(v1)}") # Uses __repr__

    v3 = v1 + v2        # Uses __add__
    print(f"Vector addition: {v3}")

    print(f"Vectors equal: {v1 == v2}")  # Uses __eq__
    print(f"Vector 1 length: {len(v1)}") # Uses __len__

def abstract_classes_demo():
    """Demonstrate abstract base classes"""
    from abc import ABC, abstractmethod

    class Vehicle(ABC):
        def __init__(self, make, model):
            self.make = make
            self.model = model

        @abstractmethod
        def start_engine(self):
            pass

        @abstractmethod
        def stop_engine(self):
            pass

    class Motorcycle(Vehicle):
        def start_engine(self):
            return f"{self.make} {self.model} motorcycle engine started"

        def stop_engine(self):
            return f"{self.make} {self.model} motorcycle engine stopped"

    class Truck(Vehicle):
        def start_engine(self):
            return f"{self.make} {self.model} truck engine started with a roar"

        def stop_engine(self):
            return f"{self.make} {self.model} truck engine stopped"

    # Usage
    motorcycle = Motorcycle("Harley-Davidson", "Sportster")
    truck = Truck("Ford", "F-150")

    print(f"Motorcycle: {motorcycle.start_engine()}")
    print(f"Truck: {truck.start_engine()}")

if __name__ == "__main__":
    main()
