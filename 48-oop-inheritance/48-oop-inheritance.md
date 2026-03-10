# 48-oop-inheritance

## Overview

Inheritance is one of the fundamental concepts of Object-Oriented Programming (OOP) that allows a class (child or subclass) to inherit attributes and methods from another class (parent or superclass). This promotes code reusability, establishes relationships between classes, and enables polymorphism. Python supports single inheritance, multiple inheritance, and provides powerful tools for managing inheritance hierarchies.

## Learning Objectives

- Understand the concept of inheritance and its benefits
- Learn how to create subclasses that inherit from parent classes
- Master method overriding and the use of `super()`
- Explore multiple inheritance and Method Resolution Order (MRO)
- Understand `isinstance()` and `issubclass()` functions
- Learn about composition vs inheritance
- Explore best practices and common patterns

## Code Examples

### Basic Inheritance

```python
class Animal:
    """Parent class (superclass)"""
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return "Some generic animal sound"

    def eat(self):
        return f"{self.name} is eating"

    def sleep(self):
        return f"{self.name} is sleeping"

    def get_info(self):
        return f"{self.name} is a {self.species}"

class Dog(Animal):
    """Child class (subclass) that inherits from Animal"""
    def __init__(self, name, breed):
        # Call parent class constructor
        super().__init__(name, "Dog")
        # Add child-specific attributes
        self.breed = breed

    # Override parent method
    def make_sound(self):
        return "Woof!"

    # Add child-specific method
    def fetch(self):
        return f"{self.name} is fetching the ball"

class Cat(Animal):
    """Another child class"""
    def make_sound(self):
        return "Meow!"

# Usage
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Siamese")

print(dog.get_info())      # "Buddy is a Dog"
print(dog.make_sound())    # "Woof!" (overridden)
print(dog.eat())           # "Buddy is eating" (inherited)
print(dog.fetch())         # "Buddy is fetching the ball" (child-specific)

print(cat.get_info())      # "Whiskers is a Siamese"
print(cat.make_sound())    # "Meow!" (overridden)
print(cat.sleep())         # "Whiskers is sleeping" (inherited)
```

### Method Overriding and super()

```python
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        return f"{self.year} {self.make} {self.model} is starting"

    def stop(self):
        return f"{self.year} {self.make} {self.model} is stopping"

    def get_description(self):
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        # Call parent constructor with super()
        super().__init__(make, model, year)
        self.num_doors = num_doors

    # Override start method but call parent method too
    def start(self):
        parent_message = super().start()
        return f"{parent_message} with {self.num_doors} doors"

    # Add car-specific method
    def drive(self):
        return f"The {self.make} {self.model} is driving on the road"

class ElectricCar(Car):
    def __init__(self, make, model, year, num_doors, battery_range):
        super().__init__(make, model, year, num_doors)
        self.battery_range = battery_range

    def start(self):
        parent_message = super().start()
        return f"{parent_message} silently (electric motor)"

    def charge(self):
        return f"Charging the {self.make} {self.model} ({self.battery_range} miles range)"

# Usage
regular_car = Car("Toyota", "Camry", 2020, 4)
electric_car = ElectricCar("Tesla", "Model 3", 2023, 4, 358)

print(regular_car.start())
print(regular_car.drive())
print()

print(electric_car.start())
print(electric_car.charge())
print(electric_car.get_description())  # Inherited from Vehicle
```

### Multiple Inheritance

```python
class Flyable:
    def fly(self):
        return "Flying through the air"

    def get_altitude(self):
        return "Current altitude: 10,000 feet"

class Swimmable:
    def swim(self):
        return "Swimming in the water"

    def get_depth(self):
        return "Current depth: 50 feet"

class Duck(Flyable, Swimmable):
    def __init__(self, name):
        self.name = name

    def quack(self):
        return "Quack!"

    # Override fly method from Flyable
    def fly(self):
        return f"{self.name} is flying gracefully"

class Penguin(Swimmable):
    def __init__(self, name):
        self.name = name

    def waddle(self):
        return f"{self.name} is waddling"

# Usage
duck = Duck("Donald")
penguin = Penguin("Pingu")

print(f"Duck: {duck.quack()}")
print(f"Duck flying: {duck.fly()}")
print(f"Duck swimming: {duck.swim()}")
print(f"Duck altitude: {duck.get_altitude()}")
print()

print(f"Penguin: {penguin.waddle()}")
print(f"Penguin swimming: {penguin.swim()}")
print(f"Penguin depth: {penguin.get_depth()}")

# Check Method Resolution Order (MRO)
print(f"\nDuck MRO: {Duck.__mro__}")
print(f"Penguin MRO: {Penguin.__mro__}")
```

### isinstance() and issubclass()

```python
class Animal:
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Dog(Mammal):
    pass

class Cat(Mammal):
    pass

class Eagle(Bird):
    pass

# Create instances
dog = Dog()
cat = Cat()
eagle = Eagle()

# isinstance() checks if an object is an instance of a class or its subclasses
print("isinstance() checks:")
print(f"dog is instance of Dog: {isinstance(dog, Dog)}")      # True
print(f"dog is instance of Mammal: {isinstance(dog, Mammal)}")  # True
print(f"dog is instance of Animal: {isinstance(dog, Animal)}")  # True
print(f"dog is instance of Bird: {isinstance(dog, Bird)}")      # False
print()

# issubclass() checks if a class is a subclass of another class
print("issubclass() checks:")
print(f"Dog is subclass of Mammal: {issubclass(Dog, Mammal)}")    # True
print(f"Dog is subclass of Animal: {issubclass(Dog, Animal)}")    # True
print(f"Dog is subclass of Bird: {issubclass(Dog, Bird)}")        # False
print(f"Mammal is subclass of Animal: {issubclass(Mammal, Animal)}")  # True
print()

# Practical usage
def animal_sound(animal):
    if isinstance(animal, Dog):
        return "Woof!"
    elif isinstance(animal, Cat):
        return "Meow!"
    elif isinstance(animal, Eagle):
        return "Screech!"
    else:
        return "Unknown animal sound"

print("Animal sounds:")
print(f"Dog: {animal_sound(dog)}")
print(f"Cat: {animal_sound(cat)}")
print(f"Eagle: {animal_sound(eagle)}")
```

### Abstract Base Classes

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class for shapes"""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        """Calculate area - must be implemented by subclasses"""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter - must be implemented by subclasses"""
        pass

    def get_description(self):
        return f"This is a {self.name}"

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        super().__init__("Triangle")
        self.base = base
        self.height = height
        self.sides = [side1, side2, side3]

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return sum(self.sides)

# Usage
shapes = [
    Rectangle(4, 5),
    Circle(3),
    Triangle(6, 4, 3, 4, 5)
]

print("Shape calculations:")
for shape in shapes:
    print(f"{shape.get_description()}:")
    print(f"  Area: {shape.area():.2f}")
    print(f"  Perimeter: {shape.perimeter():.2f}")
    print()

# This would raise an error - can't instantiate abstract class
try:
    shape = Shape("Generic")
except TypeError as e:
    print(f"Error: {e}")
```

### Composition vs Inheritance

```python
# Inheritance approach (IS-A relationship)
class Engine:
    def start(self):
        return "Engine starting"

    def stop(self):
        return "Engine stopping"

class CarWithInheritance(Engine):
    def drive(self):
        return "Car is driving"

# Composition approach (HAS-A relationship)
class CarWithComposition:
    def __init__(self):
        self.engine = Engine()  # Car HAS-A Engine

    def start(self):
        return self.engine.start()

    def stop(self):
        return self.engine.stop()

    def drive(self):
        return "Car is driving"

# Another composition example
class Person:
    def __init__(self, name):
        self.name = name

class Address:
    def __init__(self, street, city, country):
        self.street = street
        self.city = city
        self.country = country

    def get_full_address(self):
        return f"{self.street}, {self.city}, {self.country}"

class PersonWithAddress:
    def __init__(self, name, address):
        self.name = name
        self.address = address  # Person HAS-A Address

    def get_info(self):
        return f"{self.name} lives at {self.address.get_full_address()}"

# Usage
# Inheritance
car1 = CarWithInheritance()
print(f"Inheritance: {car1.start()}, {car1.drive()}")

# Composition
car2 = CarWithComposition()
print(f"Composition: {car2.start()}, {car2.drive()}")

# Composition with multiple objects
address = Address("123 Main St", "Anytown", "USA")
person = PersonWithAddress("John Doe", address)
print(f"Person info: {person.get_info()}")
```

### Advanced Inheritance Patterns

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_info(self):
        return f"{self.name}: ${self.salary}"

    def work(self):
        return f"{self.name} is working"

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
        self.subordinates = []

    def add_subordinate(self, employee):
        self.subordinates.append(employee)

    def work(self):
        return f"{self.name} is managing the {self.department} department"

    def get_team_info(self):
        info = f"Manager: {self.name}\nTeam members:"
        for emp in self.subordinates:
            info += f"\n  - {emp.get_info()}"
        return info

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def work(self):
        return f"{self.name} is coding in {self.programming_language}"

    def debug(self):
        return f"{self.name} is debugging {self.programming_language} code"

class SeniorDeveloper(Developer):
    def __init__(self, name, salary, programming_language, years_experience):
        super().__init__(name, salary, programming_language)
        self.years_experience = years_experience

    def mentor(self):
        return f"{self.name} is mentoring junior developers"

    def work(self):
        return f"{self.name} is architecting {self.programming_language} solutions"

# Usage
manager = Manager("Alice", 80000, "Engineering")
dev1 = Developer("Bob", 60000, "Python")
dev2 = Developer("Charlie", 65000, "JavaScript")
senior_dev = SeniorDeveloper("David", 90000, "Python", 8)

# Build team hierarchy
manager.add_subordinate(dev1)
manager.add_subordinate(dev2)
manager.add_subordinate(senior_dev)

# Demonstrate polymorphism
employees = [manager, dev1, dev2, senior_dev]

print("Employee work activities:")
for emp in employees:
    print(f"- {emp.work()}")

print(f"\n{manager.get_team_info()}")

print(f"\nSenior developer activities:")
print(f"- {senior_dev.work()}")
print(f"- {senior_dev.mentor()}")
print(f"- {senior_dev.debug()}")
```

## Understanding Inheritance

### Types of Inheritance

1. **Single Inheritance**: One child class inherits from one parent class
2. **Multiple Inheritance**: One child class inherits from multiple parent classes
3. **Multilevel Inheritance**: A child class inherits from a parent class, which itself inherits from another class
4. **Hierarchical Inheritance**: Multiple child classes inherit from the same parent class

### Method Resolution Order (MRO)

- Determines the order in which methods are searched in inheritance hierarchies
- Uses C3 linearization algorithm in Python
- Can be viewed using `ClassName.__mro__` or `ClassName.mro()`

### super() Function

- Allows calling methods from parent classes
- Essential for proper initialization in inheritance chains
- Enables cooperative inheritance patterns

### Abstract Base Classes (ABC)

- Define interfaces that must be implemented by subclasses
- Use `@abstractmethod` decorator
- Cannot be instantiated directly
- Ensure consistent APIs across related classes

### Composition vs Inheritance

- **Inheritance**: Use when there's an "IS-A" relationship
- **Composition**: Use when there's a "HAS-A" relationship
- **Composition** is often more flexible than inheritance
- **Composition** avoids some inheritance-related problems

### Best Practices

1. Use inheritance for "IS-A" relationships
2. Keep inheritance hierarchies shallow
3. Use `super()` for proper method chaining
4. Don't override methods unless necessary
5. Use abstract base classes for interfaces
6. Prefer composition over inheritance when possible
7. Use `isinstance()` and `issubclass()` judiciously

### Common Patterns

- **Template Method**: Parent defines algorithm structure, children implement details
- **Factory Method**: Parent defines creation interface, children implement creation
- **Strategy**: Different algorithms encapsulated in different classes
- **Decorator**: Add functionality to objects dynamically

## Notes

- Inheritance establishes "IS-A" relationships between classes
- Child classes inherit all attributes and methods from parent classes
- Method overriding allows child classes to provide specific implementations
- `super()` enables calling parent class methods
- Multiple inheritance is supported but should be used carefully
- Abstract base classes ensure interface compliance
- Composition is often preferred over deep inheritance hierarchies
- Understanding MRO is crucial for multiple inheritance
- Inheritance should be used to model real-world relationships, not just for code reuse
