# 47-oop-class-variables

## Overview

Class variables are variables that are shared among all instances (objects) of a class. Unlike instance variables that are unique to each object, class variables maintain the same value across all instances and can be accessed without creating an instance of the class. Understanding class variables is crucial for managing shared state and constants in object-oriented programming.

## Learning Objectives

- Understand the difference between class variables and instance variables
- Learn how to define and access class variables
- Master the behavior of class variables when modified
- Explore common use cases and best practices
- Understand potential pitfalls and how to avoid them

## Code Examples

### Basic Class Variables

```python
class Car:
    # Class variables (shared by all instances)
    wheels = 4  # All cars have 4 wheels
    vehicle_type = "Automobile"  # All cars are automobiles

    def __init__(self, make, model, year):
        # Instance variables (unique to each instance)
        self.make = make
        self.model = model
        self.year = year

# Accessing class variables
print(f"All cars have {Car.wheels} wheels")  # 4
print(f"Vehicle type: {Car.vehicle_type}")   # Automobile

# Creating instances
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2019)

# Class variables are accessible through instances too
print(f"Car1 wheels: {car1.wheels}")  # 4
print(f"Car2 wheels: {car2.wheels}")  # 4

# But instance variables are unique
print(f"Car1: {car1.make} {car1.model}")  # Toyota Camry
print(f"Car2: {car2.make} {car2.model}")  # Honda Civic
```

### Class Variables for Counting Instances

```python
class Student:
    # Class variable to count total students
    total_students = 0

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        # Increment the class variable when a new student is created
        Student.total_students += 1

    def get_info(self):
        return f"{self.name} is in grade {self.grade}"

# Create some students
student1 = Student("Alice", 10)
student2 = Student("Bob", 11)
student3 = Student("Charlie", 9)

print(f"Total students: {Student.total_students}")  # 3
print(f"Student 1: {student1.get_info()}")
print(f"Student 2: {student2.get_info()}")
print(f"Student 3: {student3.get_info()}")

# The class variable is shared
print(f"Accessing through instance: {student1.total_students}")  # 3
print(f"Accessing through class: {Student.total_students}")     # 3
```

### Modifying Class Variables

```python
class Company:
    # Class variables
    company_name = "Tech Corp"
    employee_count = 0
    default_salary = 50000

    def __init__(self, name, salary=None):
        self.name = name
        # Use class variable as default if no salary provided
        self.salary = salary if salary is not None else Company.default_salary
        Company.employee_count += 1

    def get_info(self):
        return f"{self.name} works at {Company.company_name} with salary ${self.salary}"

# Create employees
emp1 = Company("Alice")
emp2 = Company("Bob", 60000)

print(f"Company: {Company.company_name}")
print(f"Employee count: {Company.employee_count}")
print(f"Default salary: ${Company.default_salary}")
print()

print(emp1.get_info())
print(emp2.get_info())
print()

# Modify class variable - affects all instances
Company.company_name = "Super Tech Corp"
print("After changing company name:")
print(emp1.get_info())
print(emp2.get_info())
print()

# Modify default salary - affects future instances
Company.default_salary = 55000
emp3 = Company("Charlie")  # Will use new default salary
print(f"New employee: {emp3.get_info()}")
```

### Class Variables vs Instance Variables

```python
class BankAccount:
    # Class variables
    bank_name = "Global Bank"
    total_accounts = 0
    interest_rate = 0.05  # 5% interest

    def __init__(self, owner, initial_balance=0):
        # Instance variables
        self.owner = owner
        self.balance = initial_balance
        BankAccount.total_accounts += 1

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return f"{self.owner}'s balance: ${self.balance:.2f}"

    @classmethod
    def get_bank_info(cls):
        return f"{cls.bank_name} has {cls.total_accounts} accounts with {cls.interest_rate*100}% interest rate"

# Create accounts
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 500)

print(f"Bank: {BankAccount.bank_name}")
print(f"Total accounts: {BankAccount.total_accounts}")
print(f"Interest rate: {BankAccount.interest_rate*100}%")
print()

print(account1.get_balance())
print(account2.get_balance())
print()

# Instance variables are independent
account1.deposit(500)
print(f"After deposit: {account1.get_balance()}")
print(f"Bob's balance unchanged: {account2.get_balance()}")
print()

# Class variables are shared
print(f"Bank info: {BankAccount.get_bank_info()}")

# Changing class variable affects all
BankAccount.interest_rate = 0.06
print(f"New interest rate: {BankAccount.interest_rate*100}%")
```

### Class Constants and Shared State

```python
class GameCharacter:
    # Class constants
    MAX_HEALTH = 100
    STARTING_LEVEL = 1

    # Shared game state
    total_characters = 0
    game_difficulty = "normal"

    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.health = GameCharacter.MAX_HEALTH  # Use class constant
        self.level = GameCharacter.STARTING_LEVEL  # Use class constant
        GameCharacter.total_characters += 1

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def heal(self, amount):
        self.health = min(self.health + amount, GameCharacter.MAX_HEALTH)

    def level_up(self):
        self.level += 1

    def get_status(self):
        return f"{self.name} ({self.character_class}) - Level {self.level}, Health: {self.health}/{GameCharacter.MAX_HEALTH}"

    @classmethod
    def change_difficulty(cls, new_difficulty):
        cls.game_difficulty = new_difficulty

    @classmethod
    def get_game_stats(cls):
        return f"Total characters: {cls.total_characters}, Difficulty: {cls.game_difficulty}"

# Create characters
hero = GameCharacter("Aragorn", "Warrior")
mage = GameCharacter("Gandalf", "Mage")

print(f"Max health constant: {GameCharacter.MAX_HEALTH}")
print(f"Starting level constant: {GameCharacter.STARTING_LEVEL}")
print()

print(hero.get_status())
print(mage.get_status())
print()

# Damage and heal
hero.take_damage(30)
mage.take_damage(20)
print("After taking damage:")
print(hero.get_status())
print(mage.get_status())
print()

mage.heal(50)
print("After mage healing:")
print(mage.get_status())
print()

# Level up
hero.level_up()
print("After hero leveling up:")
print(hero.get_status())
print()

# Game stats
print(f"Game stats: {GameCharacter.get_game_stats()}")

# Change difficulty
GameCharacter.change_difficulty("hard")
print(f"New difficulty: {GameCharacter.game_difficulty}")
```

### Potential Pitfalls with Class Variables

```python
class ProblematicClass:
    # Class variable that can cause issues
    shared_list = []  # This is shared by all instances!

    def __init__(self, name):
        self.name = name
        # This modifies the shared list for ALL instances!
        self.shared_list.append(name)

    def get_shared_list(self):
        return self.shared_list

# This demonstrates the problem
obj1 = ProblematicClass("Alice")
obj2 = ProblematicClass("Bob")

print(f"Obj1 shared list: {obj1.get_shared_list()}")  # ['Alice', 'Bob']
print(f"Obj2 shared list: {obj2.get_shared_list()}")  # ['Alice', 'Bob'] - Same list!
print(f"Are they the same object? {obj1.shared_list is obj2.shared_list}")  # True

print()

# Better approach
class BetterClass:
    def __init__(self, name):
        self.name = name
        # Instance variable - each object gets its own list
        self.my_list = []

    def add_item(self, item):
        self.my_list.append(item)

    def get_my_list(self):
        return self.my_list

obj3 = BetterClass("Charlie")
obj4 = BetterClass("David")

obj3.add_item("item1")
obj4.add_item("item2")

print(f"Obj3 list: {obj3.get_my_list()}")  # ['item1']
print(f"Obj4 list: {obj4.get_my_list()}")  # ['item2']
print(f"Are they the same object? {obj3.my_list is obj4.my_list}")  # False
```

### Best Practices for Class Variables

```python
class BestPracticesExample:
    # Use ALL_CAPS for constants
    MAX_CONNECTIONS = 100
    DEFAULT_TIMEOUT = 30

    # Use descriptive names for shared state
    total_instances = 0
    active_connections = 0

    def __init__(self, name):
        self.name = name
        # Always use the class name to modify class variables
        BestPracticesExample.total_instances += 1

    @classmethod
    def get_instance_count(cls):
        return cls.total_instances

    @classmethod
    def reset_counters(cls):
        cls.total_instances = 0
        cls.active_connections = 0

    def connect(self):
        if BestPracticesExample.active_connections < BestPracticesExample.MAX_CONNECTIONS:
            BestPracticesExample.active_connections += 1
            return True
        return False

    def disconnect(self):
        if BestPracticesExample.active_connections > 0:
            BestPracticesExample.active_connections -= 1

# Usage
print(f"Max connections: {BestPracticesExample.MAX_CONNECTIONS}")
print(f"Default timeout: {BestPracticesExample.DEFAULT_TIMEOUT}")

instances = [BestPracticesExample(f"Instance{i}") for i in range(3)]
print(f"Total instances: {BestPracticesExample.get_instance_count()}")

# Test connections
for instance in instances:
    if instance.connect():
        print(f"{instance.name} connected")
    else:
        print(f"{instance.name} failed to connect")

print(f"Active connections: {BestPracticesExample.active_connections}")

# Disconnect one
instances[0].disconnect()
print(f"After disconnect: {BestPracticesExample.active_connections}")
```

## Understanding Class Variables

### Class Variables vs Instance Variables

| Aspect           | Class Variables                             | Instance Variables         |
| ---------------- | ------------------------------------------- | -------------------------- |
| **Definition**   | Defined outside `__init__`                  | Defined in `__init__`      |
| **Scope**        | Shared by all instances                     | Unique to each instance    |
| **Access**       | `ClassName.variable` or `instance.variable` | `instance.variable` only   |
| **Modification** | Affects all instances                       | Affects only that instance |
| **Use cases**    | Constants, counters, shared state           | Object-specific data       |

### When to Use Class Variables

1. **Constants**: Values that don't change (MAX_HEALTH, DEFAULT_TIMEOUT)
2. **Counters**: Tracking total instances or shared statistics
3. **Configuration**: Shared settings that affect all instances
4. **Shared state**: Data that needs to be accessed by all instances

### When to Use Instance Variables

1. **Unique data**: Information specific to each object
2. **Mutable state**: Data that can change independently
3. **Object identity**: Properties that define what makes this object unique

### Common Pitfalls

1. **Mutable class variables**: Lists, dictionaries shared by all instances
2. **Modifying through instances**: Can create instance variables that shadow class variables
3. **Inheritance issues**: Class variables can be tricky with inheritance

### Best Practices

1. Use ALL_CAPS for constants
2. Always use the class name to access/modify class variables
3. Be careful with mutable objects as class variables
4. Use `@classmethod` decorators for class-level operations
5. Document the purpose of class variables clearly

## Notes

- Class variables are defined at the class level and shared among all instances
- Instance variables are defined in `__init__` and are unique to each instance
- Modifying a class variable through the class name affects all instances
- Modifying a class variable through an instance creates a new instance variable that shadows the class variable
- Class variables are often used for constants, counters, and shared configuration
- Be cautious with mutable objects (lists, dicts) as class variables - they can cause unexpected behavior
- Use class methods (`@classmethod`) to work with class variables
- Class variables can be accessed from both the class and instances, but should typically be modified through the class
