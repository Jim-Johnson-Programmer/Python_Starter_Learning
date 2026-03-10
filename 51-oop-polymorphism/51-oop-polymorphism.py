# ============================================================================
# 51-oop-polymorphism.py
# Polymorphism: "Many Forms" - Same method name, different behaviors
# ============================================================================

print("=" * 80)
print("EXAMPLE 1: Basic Method Overriding (Runtime Polymorphism)")
print("=" * 80)

class Animal:
    def speak(self):
        return "Some generic animal sound"
    
    def move(self):
        return "Moving..."

class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"
    
    def move(self):
        return "Running on four legs"

class Cat(Animal):
    def speak(self):
        return "Meow..."
    
    def move(self):
        return "Walking silently"

class Bird(Animal):
    def speak(self):
        return "Tweet tweet!"
    
    def move(self):
        return "Flying through the air"

# Polymorphism: Same method name, different behaviors!
animals = [Dog(), Cat(), Bird(), Animal()]

for animal in animals:
    print(f"{animal.__class__.__name__}: {animal.speak()}")
    print(f"  └─ {animal.move()}")
print()

print("=" * 80)
print("EXAMPLE 2: Shape Polymorphism with Calculation Methods")
print("=" * 80)

import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area()")
    
    def perimeter(self):
        raise NotImplementedError("Subclass must implement perimeter()")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        # Heron's formula
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self):
        return self.a + self.b + self.c

# Polymorphism in action
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4, 5)
]

print("Shape Properties:")
for shape in shapes:
    print(f"{shape.__class__.__name__}:")
    print(f"  Area:      {shape.area():.2f}")
    print(f"  Perimeter: {shape.perimeter():.2f}")
print()

print("=" * 80)
print("EXAMPLE 3: Duck Typing (Python's Polymorphism Philosophy)")
print("=" * 80)

class Guitar:
    def play(self):
        return "🎸 Playing sweet guitar riffs!"

class Violin:
    def play(self):
        return "🎻 Playing classical violin music!"

class Piano:
    def play(self):
        return "🎹 Playing beautiful piano melodies!"

class Harmonica:
    def play(self):
        return "🎵 Playing harmonica blues!"

def musician_plays(instrument):
    """Duck typing: if it has a play() method, it's an instrument!"""
    print(instrument.play())

print("✨ Duck Typing Demo - 'If it quacks like a duck, it's a duck!'")
instruments = [Guitar(), Violin(), Piano(), Harmonica()]
for instrument in instruments:
    musician_plays(instrument)
print()

print("=" * 80)
print("EXAMPLE 4: Method Overriding with super()")
print("=" * 80)

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def start(self):
        return "Engine starting..."
    
    def stop(self):
        return "Engine stopping..."

class Car(Vehicle):
    def start(self):
        parent_action = super().start()
        return f"{parent_action} Car is ready to drive!"
    
    def stop(self):
        parent_action = super().stop()
        return f"{parent_action} Car turned off."

class Motorcycle(Vehicle):
    def start(self):
        parent_action = super().start()
        return f"{parent_action} Motorcycle roaring to life!"
    
    def stop(self):
        parent_action = super().stop()
        return f"{parent_action} Motorcycle powered down."

vehicles = [Car("Toyota", "Camry"), Motorcycle("Harley", "Davidson")]
for vehicle in vehicles:
    print(f"{vehicle.brand} {vehicle.model}:")
    print(f"  {vehicle.start()}")
    print(f"  {vehicle.stop()}")
print()

print("=" * 80)
print("EXAMPLE 5: Operator Overloading - Magic Methods")
print("=" * 80)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Overload the + operator
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    # Overload the - operator
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    # Overload the * operator
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    # Overload the == operator
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    # Overload the < operator
    def __lt__(self, other):
        return (self.x ** 2 + self.y ** 2) < (other.x ** 2 + other.y ** 2)
    
    # String representation
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    # Official representation
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    # Length
    def __len__(self):
        return int(math.sqrt(self.x ** 2 + self.y ** 2))

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = Vector(1, 2)

print("Vector Operator Overloading:")
print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v2 - v1 = {v2 - v1}")
print(f"v1 * 3 = {v1 * 3}")
print(f"v1 == v3: {v1 == v3}")
print(f"v1 < v2: {v1 < v2}")
print(f"Length of v1: {len(v1)}")
print()

print("=" * 80)
print("EXAMPLE 6: Bank Account Polymorphism")
print("=" * 80)

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"
    
    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest applied: ${interest:.2f}. New balance: ${self.balance:.2f}"

class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            return "Exceeded overdraft limit!"
        self.balance -= amount
        if self.balance < 0:
            return f"Withdrew ${amount}. Warning: Overdraft! Balance: ${self.balance}"
        return f"Withdrew ${amount}. New balance: ${self.balance}"

print("Bank Account Polymorphism:")
savings = SavingsAccount("SAV001", 1000, 0.05)
checking = CheckingAccount("CHK001", 500, 200)

print(f"Savings Account: {savings.deposit(500)}")
print(f"  {savings.apply_interest()}")
print()
print(f"Checking Account: {checking.withdraw(600)}")
print(f"  {checking.withdraw(100)}")
print()

print("=" * 80)
print("EXAMPLE 7: Payment Processing - Real World Example")
print("=" * 80)

class PaymentProcessor:
    def process_payment(self, amount):
        raise NotImplementedError("Subclass must implement process_payment()")
    
    def refund(self, amount):
        raise NotImplementedError("Subclass must implement refund()")

class CreditCardProcessor(PaymentProcessor):
    def __init__(self, card_number):
        self.card_number = card_number
    
    def process_payment(self, amount):
        return f"💳 Credit Card ({self.card_number[-4:]}): Processing ${amount} payment"
    
    def refund(self, amount):
        return f"💳 Credit Card: Refunding ${amount}"

class PayPalProcessor(PaymentProcessor):
    def __init__(self, email):
        self.email = email
    
    def process_payment(self, amount):
        return f"🌐 PayPal ({self.email}): Processing ${amount} payment"
    
    def refund(self, amount):
        return f"🌐 PayPal: Refunding ${amount}"

class BitcoinProcessor(PaymentProcessor):
    def __init__(self, wallet):
        self.wallet = wallet
    
    def process_payment(self, amount):
        return f"₿ Bitcoin ({self.wallet}): Processing {amount} BTC"
    
    def refund(self, amount):
        return f"₿ Bitcoin: Refunding {amount} BTC"

# Polymorphism: Process different payment types the same way
def checkout(processor, amount):
    print(processor.process_payment(amount))

print("Payment Processing System:")
processors = [
    CreditCardProcessor("1234567890123456"),
    PayPalProcessor("user@example.com"),
    BitcoinProcessor("1A1z7agoat5...")
]

for processor in processors:
    checkout(processor, 100)
print()

print("=" * 80)
print("EXAMPLE 8: String Representation - __str__ vs __repr__")
print("=" * 80)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

person = Person("Alice", 30)
print(f"str():  {str(person)}")
print(f"repr(): {repr(person)}")
print(f"print(): ", end="")
print(person)
print()

print("=" * 80)
print("EXAMPLE 9: Comparison Operators - __eq__, __lt__, __gt__")
print("=" * 80)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __eq__(self, other):
        return self.price == other.price
    
    def __lt__(self, other):
        return self.price < other.price
    
    def __gt__(self, other):
        return self.price > other.price
    
    def __str__(self):
        return f"{self.name} (${self.price})"

products = [
    Product("Laptop", 999),
    Product("Mouse", 25),
    Product("Monitor", 300),
]

print("Products sorted by price:")
for product in sorted(products):
    print(f"  {product}")

p1 = Product("Keyboard", 80)
p2 = Product("Mouse", 80)
print(f"\nKeyboard == Mouse (same price)? {p1 == p2}")
print()

print("=" * 80)
print("EXAMPLE 10: Container Emulation - __len__ and __getitem__")
print("=" * 80)

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
    
    def add_song(self, song):
        self.songs.append(song)
    
    def __len__(self):
        return len(self.songs)
    
    def __getitem__(self, index):
        return self.songs[index]
    
    def __str__(self):
        return f"Playlist: {self.name}"

playlist = Playlist("My Favorites")
playlist.add_song("Imagine")
playlist.add_song("Bohemian Rhapsody")
playlist.add_song("Stairway to Heaven")

print(f"Playlist: {playlist}")
print(f"Number of songs: {len(playlist)}")
print(f"First song: {playlist[0]}")
print(f"All songs:")
for i in range(len(playlist)):
    print(f"  {i+1}. {playlist[i]}")
print()

print("=" * 80)
print("SUMMARY - KEY POINTS ABOUT POLYMORPHISM")
print("=" * 80)
print("""
✅ What is Polymorphism?
   "Many Forms" - Same method name, different behaviors based on object type

📋 Types of Polymorphism:
   1. Method Overriding (runtime polymorphism)
      - Child classes override parent methods
      - Python determines which method to call at runtime
   
   2. Duck Typing (Python's philosophy)
      - "If it quacks like a duck, it's a duck"
      - Any object with required methods can be used
   
   3. Operator Overloading (magic methods)
      - __add__, __sub__, __mul__, etc.
      - Makes objects work with Python operators

🎯 Common Magic Methods:
   __str__()   : String representation for users
   __repr__()  : Developer-friendly representation
   __add__()   : Overload + operator
   __sub__()   : Overload - operator
   __eq__()    : Overload == operator
   __lt__()    : Overload < operator
   __len__()   : Overload len() function
   __getitem__(): Overload [] operator

💡 Benefits:
   - Flexible code that works with multiple types
   - Easy to extend with new classes
   - Cleaner, more maintainable code
   - Follows Python's "duck typing" philosophy

⚠️ Best Practices:
   - Use polymorphism to make code flexible and reusable
   - Override methods meaningfully
   - Use magic methods to make custom objects behave like built-ins
   - Document which methods can be overridden
   - Keep method contracts consistent with parent classes
""")
