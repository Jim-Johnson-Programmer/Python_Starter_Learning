# ============================================================================
# 50-oop-super-method.py
# The super() method allows you to call methods from a parent class
# ============================================================================

print("=" * 80)
print("EXAMPLE 1: Basic Inheritance Without super()")
print("=" * 80)

class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal initialized: {name}")
    
    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def __init__(self, name, breed):
        # ❌ NOT using super() - hardcodes the parent class name
        Animal.__init__(self, name)
        self.breed = breed
        print(f"Dog initialized: {breed}")
    
    def speak(self):
        Animal.speak(self)  # Hardcoded parent call
        print(f"{self.name} barks!")

dog1 = Dog("Rex", "Labrador")
dog1.speak()
print()

print("=" * 80)
print("EXAMPLE 2: Basic Inheritance With super()")
print("=" * 80)

class Cat(Animal):
    def __init__(self, name, color):
        # ✅ Using super() - more flexible and cleaner
        super().__init__(name)
        self.color = color
        print(f"Cat initialized: {color}")
    
    def speak(self):
        super().speak()  # Uses super() - cleaner!
        print(f"{self.name} meows!")

cat1 = Cat("Whiskers", "Orange")
cat1.speak()
print()

print("=" * 80)
print("EXAMPLE 3: Multi-Level Inheritance")
print("=" * 80)

class Mammal(Animal):
    def __init__(self, name, temperature):
        super().__init__(name)
        self.body_temperature = temperature
        print(f"Mammal body temperature: {temperature}°C")

class Whale(Mammal):
    def __init__(self, name, temperature, ocean):
        super().__init__(name, temperature)
        self.ocean = ocean
        print(f"Whale lives in: {ocean}")
    
    def speak(self):
        super().speak()
        print(f"{self.name} makes whale sounds!")

whale = Whale("Moby", 37, "Atlantic")
whale.speak()
print()

print("=" * 80)
print("EXAMPLE 4: Real-World Example - Employee Hierarchy")
print("=" * 80)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person created: {name}, Age: {age}")
    
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old"

class Employee(Person):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.department = department
        print(f"Employee ID: {employee_id}, Department: {department}")
    
    def introduce(self):
        parent_intro = super().introduce()
        return f"{parent_intro}. I work in {self.department} (ID: {self.employee_id})"

class Manager(Employee):
    def __init__(self, name, age, employee_id, department, team_size):
        super().__init__(name, age, employee_id, department)
        self.team_size = team_size
        print(f"Manager overseeing {team_size} people")
    
    def introduce(self):
        employee_intro = super().introduce()
        return f"{employee_intro}. I manage {self.team_size} people."

manager = Manager("Sarah", 35, "E001", "Engineering", 5)
print(manager.introduce())
print()

print("=" * 80)
print("EXAMPLE 5: Multiple Inheritance with super()")
print("=" * 80)

class Vehicle:
    def describe(self):
        print("I am a vehicle")

class Electric:
    def describe(self):
        print("I use electricity")

class HybridCar(Vehicle, Electric):
    def describe(self):
        print("Describing a hybrid car:")
        super().describe()
        print("I am a hybrid car")
    
    def show_mro(self):
        print("\nMethod Resolution Order (MRO):")
        for cls in HybridCar.__mro__:
            print(f"  - {cls.__name__}")

hybrid = HybridCar()
hybrid.describe()
hybrid.show_mro()
print()

print("=" * 80)
print("EXAMPLE 6: Complex Multiple Inheritance (Diamond Problem)")
print("=" * 80)

class A:
    def method(self):
        print("A's method")

class B(A):
    def method(self):
        print("B's method")
        super().method()

class C(A):
    def method(self):
        print("C's method")
        super().method()

class D(B, C):
    def method(self):
        print("D's method")
        super().method()

print("Calling D().method():")
d = D()
d.method()

print("\nMRO for class D:")
print("D -> " + " -> ".join([cls.__name__ for cls in D.__mro__[1:]]))
print()

print("=" * 80)
print("EXAMPLE 7: super() with Arguments (Python 2 compatibility)")
print("=" * 80)

class Parent:
    def __init__(self, value):
        self.value = value
        print(f"Parent initialized with value: {value}")

class Child(Parent):
    def __init__(self, value, extra):
        # Both forms work in Python 3:
        # super().__init__(value)  # Implicit form (Python 3)
        super(Child, self).__init__(value)  # Explicit form (Python 2/3)
        self.extra = extra
        print(f"Child initialized with extra: {extra}")

child = Child("Hello", "World")
print()

print("=" * 80)
print("EXAMPLE 8: Avoiding super() Issues")
print("=" * 80)

class Good:
    def operation(self):
        print("Good: Starting operation")
    
    def __init__(self):
        self.operation()

class GoodChild(Good):
    def __init__(self):
        super().__init__()  # ✅ Calls parent first
    
    def operation(self):
        print("GoodChild: Enhanced operation")
        super().operation()

print("✅ Good Example (using super()):")
good = GoodChild()
print()

class Bad:
    def setup(self):
        print("Bad: Setup initiated")

class BadChild(Bad):
    def setup(self):
        print("BadChild: Setup")
        # If we don't call super().setup(), parent's setup is skipped!
        # This can cause issues if parent's setup is critical

print("⚠️  Bad Example (not using super()):")
bad = BadChild()
bad.setup()
print("^ Notice: Bad.setup() was never called!")
print()

print("=" * 80)
print("EXAMPLE 9: Accessing Parent Properties")
print("=" * 80)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class ColoredRectangle(Rectangle):
    def __init__(self, width, height, color):
        super().__init__(width, height)
        self.color = color
    
    def describe(self):
        # Access parent's properties through parent method
        parent_area = super().area()
        return f"A {self.color} rectangle: {self.width}x{self.height}, Area: {parent_area}"

rect = ColoredRectangle(5, 10, "red")
print(rect.describe())
print()

print("=" * 80)
print("EXAMPLE 10: When NOT to Use super()")
print("=" * 80)

# super() is great for inheritance, but if you DON'T inherit, you don't need it!

class StandaloneClass:
    def method(self):
        print("Standalone - no parent to call")

standalone = StandaloneClass()
standalone.method()
print()

print("=" * 80)
print("SUMMARY - KEY POINTS ABOUT super()")
print("=" * 80)
print("""
✅ Use super() to:
   1. Call parent class methods without hardcoding the class name
   2. Support multiple inheritance correctly (follows MRO)
   3. Make code more maintainable and flexible
   4. Ensure all parent classes in a hierarchy are properly initialized

📋 super() Syntax:
   super().method_name(arguments)
   OR
   super(ClassName, self).method_name(arguments)  # Python 2 style

🎯 Common Usage:
   - In __init__() to initialize parent classes
   - In other methods to extend parent behavior
   - In multiple inheritance situations

⚠️ Important:
   - Check MRO with ClassName.__mro__ for complex hierarchies
   - Always call super().__init__() in child class __init__()
   - Don't mix super() and direct parent calls in the same method

🚫 When NOT to use super():
   - When a class has no parent (no inheritance)
   - When you explicitly don't want to call the parent method
""")
