# 46-oop-python

## Overview

Object-Oriented Programming (OOP) is a programming paradigm that organizes code around objects and classes. Python supports OOP and provides all the standard features like classes, inheritance, polymorphism, and encapsulation. OOP helps create modular, reusable, and maintainable code by modeling real-world entities as objects.

## Learning Objectives

- Understand the basic concepts of classes and objects
- Learn how to create and use classes with methods and attributes
- Master inheritance and method overriding
- Explore polymorphism and encapsulation
- Understand class vs instance variables and methods
- Learn about special methods (magic methods) and decorators

## Code Examples

### Basic Class and Object

```python
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

print(car1.get_description())  # "2020 Toyota Camry"
print(car1.start_engine())     # "The 2020 Toyota Camry's engine is starting!"
```

### Instance Variables vs Class Variables

```python
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

print(emp1.get_info())  # "Alice works at Tech Corp with salary $50000"
print(emp2.get_info())  # "Bob works at Tech Corp with salary $60000"
print(f"Total employees: {Employee.employee_count}")  # 2
```

### Class Methods and Static Methods

```python
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
print(result)  # 8

utils = MathUtils.create_from_string("4+2")  # Class method call
print(utils.multiply())  # 8
```

### Inheritance

```python
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

print(dog.get_info())      # "Buddy is a Dog"
print(dog.make_sound())    # "Woof!"
print(dog.fetch())         # "Buddy is fetching the ball!"

print(cat.get_info())      # "Whiskers is a Siamese"
print(cat.make_sound())    # "Meow!"
```

### Multiple Inheritance

```python
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
print(duck.quack())   # "Quack!"
print(duck.fly())     # "Flying high!"
print(duck.swim())    # "Swimming gracefully!"
```

### Polymorphism

```python
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

for shape in shapes:
    print(f"Area: {shape.area():.2f}, Perimeter: {shape.perimeter():.2f}")
```

### Encapsulation with Properties

```python
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

account.withdraw(200)
print(f"After withdrawal: ${account.balance}")

# Using property setter
account.balance = 1500
print(f"After setting balance: ${account.balance}")
```

### Magic Methods (Dunder Methods)

```python
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

print(v1)           # Vector(3, 4)
print(repr(v1))     # Vector(x=3, y=3)

v3 = v1 + v2        # Uses __add__
print(v3)           # Vector(4, 6)

print(v1 == v2)     # False (uses __eq__)
print(len(v1))      # 5 (uses __len__)
```

### Abstract Base Classes

```python
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

print(motorcycle.start_engine())
print(truck.start_engine())
```

## OOP Principles

### 1. Encapsulation

- Bundling data and methods that operate on that data
- Controlling access to internal state
- Using private attributes and public methods

### 2. Inheritance

- Creating new classes from existing ones
- Reusing code and establishing relationships
- Single and multiple inheritance support

### 3. Polymorphism

- Same interface, different implementations
- Method overriding and operator overloading
- Duck typing in Python

### 4. Abstraction

- Hiding complex implementation details
- Providing simple interfaces
- Using abstract base classes

## Notes

- Everything in Python is an object
- Classes are objects too (instances of `type`)
- Use `self` to refer to instance methods and attributes
- Use `cls` for class methods
- Private attributes are indicated by single underscore (convention) or double underscore (name mangling)
- Magic methods enable operator overloading and special behaviors
- Multiple inheritance can lead to complex method resolution order (MRO)
- Abstract base classes ensure interface compliance
