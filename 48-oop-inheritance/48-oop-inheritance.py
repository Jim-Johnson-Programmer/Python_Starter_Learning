# 48-oop-inheritance
# Understanding Inheritance in Python OOP

def main():
    print("=== Inheritance Tutorial ===\n")

    # Section 1: Basic inheritance
    print("1. Basic Inheritance")
    basic_inheritance_demo()
    print()

    # Section 2: Method overriding and super()
    print("2. Method Overriding and super()")
    overriding_super_demo()
    print()

    # Section 3: Multiple inheritance
    print("3. Multiple Inheritance")
    multiple_inheritance_demo()
    print()

    # Section 4: isinstance() and issubclass()
    print("4. isinstance() and issubclass() Functions")
    type_checking_demo()
    print()

    # Section 5: Abstract base classes
    print("5. Abstract Base Classes")
    abstract_classes_demo()
    print()

    # Section 6: Composition vs inheritance
    print("6. Composition vs Inheritance")
    composition_demo()
    print()

    # Section 7: Advanced inheritance patterns
    print("7. Advanced Inheritance Patterns")
    advanced_patterns_demo()
    print()

def basic_inheritance_demo():
    """Demonstrate basic inheritance concepts"""
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

    print(f"Dog: {dog.get_info()}")
    print(f"Dog sound: {dog.make_sound()} (overridden)")
    print(f"Dog eating: {dog.eat()} (inherited)")
    print(f"Dog fetching: {dog.fetch()} (child-specific)")

    print(f"Cat: {cat.get_info()}")
    print(f"Cat sound: {cat.make_sound()} (overridden)")
    print(f"Cat sleeping: {cat.sleep()} (inherited)")

def overriding_super_demo():
    """Demonstrate method overriding and super() usage"""
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

    print(f"Regular car: {regular_car.start()}")
    print(f"Regular car: {regular_car.drive()}")
    print(f"Regular car: {regular_car.get_description()} (inherited)")

    print(f"Electric car: {electric_car.start()}")
    print(f"Electric car: {electric_car.charge()}")
    print(f"Electric car: {electric_car.get_description()} (inherited)")

def multiple_inheritance_demo():
    """Demonstrate multiple inheritance and MRO"""
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
    print(f"Duck flying: {duck.fly()} (overridden)")
    print(f"Duck swimming: {duck.swim()} (inherited)")
    print(f"Duck altitude: {duck.get_altitude()} (inherited)")

    print(f"Penguin: {penguin.waddle()}")
    print(f"Penguin swimming: {penguin.swim()} (inherited)")
    print(f"Penguin depth: {penguin.get_depth()} (inherited)")

    # Check Method Resolution Order (MRO)
    print(f"\nDuck MRO: {Duck.__mro__}")
    print(f"Penguin MRO: {Penguin.__mro__}")

def type_checking_demo():
    """Demonstrate isinstance() and issubclass() functions"""
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
    print(f"dog is instance of Dog: {isinstance(dog, Dog)}")
    print(f"dog is instance of Mammal: {isinstance(dog, Mammal)}")
    print(f"dog is instance of Animal: {isinstance(dog, Animal)}")
    print(f"dog is instance of Bird: {isinstance(dog, Bird)}")

    # issubclass() checks if a class is a subclass of another class
    print("\nissubclass() checks:")
    print(f"Dog is subclass of Mammal: {issubclass(Dog, Mammal)}")
    print(f"Dog is subclass of Animal: {issubclass(Dog, Animal)}")
    print(f"Dog is subclass of Bird: {issubclass(Dog, Bird)}")
    print(f"Mammal is subclass of Animal: {issubclass(Mammal, Animal)}")

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

    print("\nAnimal sounds:")
    print(f"Dog: {animal_sound(dog)}")
    print(f"Cat: {animal_sound(cat)}")
    print(f"Eagle: {animal_sound(eagle)}")

def abstract_classes_demo():
    """Demonstrate abstract base classes"""
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

    # This would raise an error - can't instantiate abstract class
    print("\nTrying to instantiate abstract class:")
    try:
        shape = Shape("Generic")
    except TypeError as e:
        print(f"Error: {e}")

def composition_demo():
    """Demonstrate composition vs inheritance"""
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
    print("Inheritance approach:")
    car1 = CarWithInheritance()
    print(f"  {car1.start()}, {car1.drive()}")

    print("Composition approach:")
    car2 = CarWithComposition()
    print(f"  {car2.start()}, {car2.drive()}")

    print("Composition with multiple objects:")
    address = Address("123 Main St", "Anytown", "USA")
    person = PersonWithAddress("John Doe", address)
    print(f"  {person.get_info()}")

def advanced_patterns_demo():
    """Demonstrate advanced inheritance patterns"""
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

if __name__ == "__main__":
    main()
