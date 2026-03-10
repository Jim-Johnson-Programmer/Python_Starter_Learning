# 51 - OOP: Polymorphism

## Overview

Polymorphism literally means "many forms" (poly = many, morph = form). In object-oriented programming, polymorphism allows you to write code that can work with objects of different types. The same method name can behave differently depending on the object calling it, making your code more flexible and reusable.

## Learning Objectives

- Understand what polymorphism is and why it's useful
- Learn the two main types of polymorphism: compile-time and runtime
- Understand method overriding in inheritance hierarchies
- Learn about duck typing in Python
- Understand operator overloading and magic methods
- Learn how polymorphism enables flexible, maintainable code
- Apply polymorphism in real-world scenarios

## Key Concepts

### What is Polymorphism?

Polymorphism enables you to:

- Write generic code that works with multiple object types
- Call methods on objects without knowing their exact type
- Define methods in parent classes and override them in child classes
- Create more flexible and reusable code

### Types of Polymorphism

#### 1. **Runtime Polymorphism (Method Overriding)**

Methods are resolved at runtime based on the actual object type, not the reference type.

```python
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(shape.area())  # Calls different area() based on actual type!
```

#### 2. **Compile-Time Polymorphism (Method Overloading)**

Python doesn't support traditional method overloading, but you can achieve similar results with default arguments or `*args`.

```python
class Calculator:
    def add(self, a, b, c=0):  # Default argument
        return a + b + c

calc = Calculator()
print(calc.add(2, 3))      # Uses default c=0
print(calc.add(2, 3, 4))   # Provides all arguments
```

#### 3. **Duck Typing**

"If it walks like a duck and quacks like a duck, it's a duck!" Python allows any object with the required methods to be used interchangeably.

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def make_it_speak(animal):
    print(animal.speak())  # Works with any object that has speak()

make_it_speak(Dog())   # Woof!
make_it_speak(Cat())   # Meow!
```

### Magic Methods (Special Methods)

Magic methods allow operators to work with custom classes through operator overloading.

| Method        | Operator | Example     |
| ------------- | -------- | ----------- |
| `__add__`     | `+`      | `a + b`     |
| `__sub__`     | `-`      | `a - b`     |
| `__mul__`     | `*`      | `a * b`     |
| `__truediv__` | `/`      | `a / b`     |
| `__eq__`      | `==`     | `a == b`    |
| `__lt__`      | `<`      | `a < b`     |
| `__str__`     | `str()`  | `str(obj)`  |
| `__repr__`    | `repr()` | `repr(obj)` |
| `__len__`     | `len()`  | `len(obj)`  |
| `__getitem__` | `[]`     | `obj[0]`    |

## Method Overriding Examples

### Basic Method Overriding

```python
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):  # Override parent's speak()
        return "Woof!"

class Cat(Animal):
    def speak(self):  # Override parent's speak()
        return "Meow!"

dog = Dog()
cat = Cat()
print(dog.speak())  # Woof!
print(cat.speak())  # Meow!
```

### Overriding with super()

```python
class Vehicle:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"Vehicle: {self.name}"

class Car(Vehicle):
    def __init__(self, name, doors):
        super().__init__(name)
        self.doors = doors

    def describe(self):
        parent_desc = super().describe()
        return f"{parent_desc}, Doors: {self.doors}"
```

## Operator Overloading (Magic Methods)

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2  # Calls __add__
print(v3)     # Vector(4, 6)
```

## Real-World Example: Payment Processing

```python
class PaymentProcessor:
    def process_payment(self, amount):
        raise NotImplementedError("Subclass must implement process_payment()")

class CreditCard(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing credit card payment: ${amount}"

class PayPal(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing PayPal payment: ${amount}"

class Bitcoin(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing Bitcoin payment: {amount} BTC"

# Polymorphism in action
payments = [CreditCard(), PayPal(), Bitcoin()]
for payment in payments:
    print(payment.process_payment(100))
```

## Benefits of Polymorphism

1. **Code Reusability** - Write once, use with many types
2. **Flexibility** - Easy to add new classes without changing existing code
3. **Maintainability** - Cleaner, more organized code
4. **Extensibility** - Easily extend functionality through inheritance
5. **Loose Coupling** - Objects are independent of each other's implementation

## Best Practices

✅ **DO:**

- Use method overriding to customize behavior in child classes
- Use magic methods to make custom classes work with Python operators
- Rely on duck typing for flexible code
- Override methods meaningfully - don't just call parent's method
- Document which methods can be overridden

❌ **DON'T:**

- Override methods without a good reason
- Create deep inheritance hierarchies (hard to understand)
- Ignore duck typing by checking types with `isinstance()` unnecessarily
- Break the contract of parent class methods when overriding
- Use polymorphism to hide complex logic

## Key Takeaways

1. Polymorphism allows the same method name to behave differently across classes
2. Method overriding is the primary form of polymorphism in Python
3. Duck typing in Python allows flexibility without strict type checking
4. Magic methods enable operator overloading for custom classes
5. Polymorphism promotes flexible, maintainable, and extensible code

## See Also

- Method Overriding and Inheritance
- Duck Typing in Python
- Magic Methods and Operator Overloading
- SOLID Principles (especially Open/Closed Principle)
