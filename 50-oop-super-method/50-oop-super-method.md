# 50 - OOP: The `super()` Method

## Overview

The `super()` method is a built-in Python function that allows you to call methods from a parent (base) class from within a child (derived) class. It's particularly useful in inheritance hierarchies where you want to extend functionality while also preserving the parent class's behavior.

## Learning Objectives

- Understand what the `super()` method does and why it's useful
- Know how to call parent class methods using `super()`
- Understand the difference between explicit parent class calls and `super()`
- Learn how `super()` works with single inheritance
- Learn how `super()` works with multiple inheritance
- Understand the Method Resolution Order (MRO)
- Apply best practices when using `super()`

## Key Concepts

### What is `super()`?

`super()` returns a proxy object that delegates method calls to a parent or sibling class. It's essential in inheritance because it:

- **Avoids hardcoding the parent class name** - If you rename the parent class, your code still works
- **Supports multiple inheritance** - Ensures all parent classes are called in the correct order
- **Ensures DRY principle** - Don't Repeat Yourself - reuse parent class code instead of rewriting it

### Syntax

```python
super().method_name(args)
# OR (explicit form, for Python 2 compatibility)
super(ChildClass, self).method_name(args)
```

### Why Use `super()` Instead of Calling the Parent Class Directly?

**Without `super()` (hardcoding parent class):**

```python
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        Animal.speak(self)  # Hardcoded parent class name
        print("Dog barks")
```

**With `super()` (better approach):**

```python
class Dog(Animal):
    def speak(self):
        super().speak()  # Flexible - works even if parent class name changes
        print("Dog barks")
```

## Basic Example: Single Inheritance

### Without `super()`:

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        print(f"Vehicle initialized: {brand}")

class Car(Vehicle):
    def __init__(self, brand, model):
        Vehicle.__init__(self, brand)  # ❌ Hardcoded parent call
        self.model = model
        print(f"Car initialized: {model}")
```

### With `super()`:

```python
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # ✅ Uses super() - cleaner and more flexible
        self.model = model
        print(f"Car initialized: {model}")
```

## Multiple Inheritance with `super()`

When a class inherits from multiple parents, the order matters! Python uses **Method Resolution Order (MRO)** to determine which method to call.

```python
class Vehicle:
    def describe(self):
        print("I am a vehicle")

class Electric:
    def describe(self):
        print("I use electricity")

class EV(Vehicle, Electric):
    def describe(self):
        super().describe()  # Calls Vehicle.describe()
        print("I am an electric vehicle")

# MRO: EV -> Vehicle -> Electric -> object
# Check with: EV.__mro__
```

## Real-World Example

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old"

class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)              # Call parent's __init__
        self.employee_id = employee_id
        self.salary = salary

    def introduce(self):
        parent_intro = super().introduce()       # Call parent's introduce()
        return f"{parent_intro}. My ID is {self.employee_id}"

emp = Employee("Alice", 30, "E001", 75000)
print(emp.introduce())
# Output: Hi, I'm Alice and I'm 30 years old. My ID is E001
```

## Method Resolution Order (MRO)

When dealing with multiple inheritance, Python uses C3 Linearization to determine the method resolution order.

```python
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

d = D()
d.method()
# Output:
# D's method
# B's method
# C's method
# A's method

# Check MRO:
print(D.__mro__)
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
```

## Common Use Cases

### 1. Initialization in Child Classes

```python
class Shape:
    def __init__(self, color):
        self.color = color

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
```

### 2. Extending Parent Behavior

```python
class Database:
    def connect(self):
        print("Connecting to database...")

class SecureDatabase(Database):
    def connect(self):
        print("Checking credentials...")
        super().connect()  # Call parent's connect() first
        print("Connection secured!")
```

### 3. Cooperative Multiple Inheritance

```python
class Mixin:
    def get_info(self):
        info = super().get_info()  # Assumes another parent implements this
        return f"Mixin: {info}"

class Base:
    def get_info(self):
        return "Base Info"

class Combined(Mixin, Base):
    pass

obj = Combined()
print(obj.get_info())  # Output: Mixin: Base Info
```

## Best Practices

✅ **DO:**

- Use `super()` instead of hardcoding parent class names
- Use `super()` in cooperative multiple inheritance
- Document the MRO when using multiple inheritance
- Call `super()` in `__init__()` to ensure all parent classes are properly initialized

❌ **DON'T:**

- Mix `super()` calls with explicit parent class calls in the same method
- Assume the order of parent classes in multiple inheritance without checking MRO
- Use `super()` without understanding MRO in complex inheritance hierarchies

## Key Takeaways

1. `super()` provides access to parent class methods without hardcoding the class name
2. It's essential for multiple inheritance to work correctly
3. Python's MRO determines the order of method resolution
4. Always use `super()` in `__init__()` to ensure proper initialization chain
5. It promotes code flexibility and follows the DRY principle

## See Also

- Method Resolution Order (MRO) and `__mro__` attribute
- Multiple Inheritance in Python
- Cooperative Multiple Inheritance Design Pattern
- Diamond Problem in OOP
