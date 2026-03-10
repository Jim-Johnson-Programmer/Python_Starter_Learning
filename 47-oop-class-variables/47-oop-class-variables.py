# 47-oop-class-variables
# Understanding Class Variables in Python OOP

def main():
    print("=== Class Variables Tutorial ===\n")

    # Section 1: Basic class variables
    print("1. Basic Class Variables")
    basic_class_vars_demo()
    print()

    # Section 2: Class variables for counting
    print("2. Class Variables for Counting Instances")
    counting_demo()
    print()

    # Section 3: Modifying class variables
    print("3. Modifying Class Variables")
    modifying_demo()
    print()

    # Section 4: Class vs instance variables
    print("4. Class Variables vs Instance Variables")
    class_vs_instance_demo()
    print()

    # Section 5: Constants and shared state
    print("5. Class Constants and Shared State")
    constants_demo()
    print()

    # Section 6: Potential pitfalls
    print("6. Potential Pitfalls with Class Variables")
    pitfalls_demo()
    print()

    # Section 7: Best practices
    print("7. Best Practices for Class Variables")
    best_practices_demo()
    print()

def basic_class_vars_demo():
    """Demonstrate basic class variables"""
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
    print(f"All cars have {Car.wheels} wheels")
    print(f"Vehicle type: {Car.vehicle_type}")

    # Creating instances
    car1 = Car("Toyota", "Camry", 2020)
    car2 = Car("Honda", "Civic", 2019)

    # Class variables are accessible through instances too
    print(f"Car1 wheels: {car1.wheels}")
    print(f"Car2 wheels: {car2.wheels}")

    # But instance variables are unique
    print(f"Car1: {car1.make} {car1.model}")
    print(f"Car2: {car2.make} {car2.model}")

def counting_demo():
    """Demonstrate class variables for counting instances"""
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

    print(f"Total students: {Student.total_students}")
    print(f"Student 1: {student1.get_info()}")
    print(f"Student 2: {student2.get_info()}")
    print(f"Student 3: {student3.get_info()}")

    # The class variable is shared
    print(f"Accessing through instance: {student1.total_students}")
    print(f"Accessing through class: {Student.total_students}")

def modifying_demo():
    """Demonstrate modifying class variables"""
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

    print(f"Employee 1: {emp1.get_info()}")
    print(f"Employee 2: {emp2.get_info()}")

    # Modify class variable - affects all instances
    Company.company_name = "Super Tech Corp"
    print("After changing company name:")
    print(f"Employee 1: {emp1.get_info()}")
    print(f"Employee 2: {emp2.get_info()}")

    # Modify default salary - affects future instances
    Company.default_salary = 55000
    emp3 = Company("Charlie")  # Will use new default salary
    print(f"New employee: {emp3.get_info()}")

def class_vs_instance_demo():
    """Demonstrate class variables vs instance variables"""
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

    print(account1.get_balance())
    print(account2.get_balance())

    # Instance variables are independent
    account1.deposit(500)
    print(f"After deposit: {account1.get_balance()}")
    print(f"Bob's balance unchanged: {account2.get_balance()}")

    # Class variables are shared
    print(f"Bank info: {BankAccount.get_bank_info()}")

    # Changing class variable affects all
    BankAccount.interest_rate = 0.06
    print(f"New interest rate: {BankAccount.interest_rate*100}%")

def constants_demo():
    """Demonstrate class constants and shared state"""
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

    print(hero.get_status())
    print(mage.get_status())

    # Damage and heal
    hero.take_damage(30)
    mage.take_damage(20)
    print("After taking damage:")
    print(hero.get_status())
    print(mage.get_status())

    mage.heal(50)
    print("After mage healing:")
    print(mage.get_status())

    # Level up
    hero.level_up()
    print("After hero leveling up:")
    print(hero.get_status())

    # Game stats
    print(f"Game stats: {GameCharacter.get_game_stats()}")

    # Change difficulty
    GameCharacter.change_difficulty("hard")
    print(f"New difficulty: {GameCharacter.game_difficulty}")

def pitfalls_demo():
    """Demonstrate potential pitfalls with class variables"""
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

def best_practices_demo():
    """Demonstrate best practices for class variables"""
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

if __name__ == "__main__":
    main()
