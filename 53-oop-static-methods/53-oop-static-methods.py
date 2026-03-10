# 53-oop-static-methods
# Python learning exercise: Understanding and using static methods

# Basic Static Method Definition
class MathUtils:
    @staticmethod
    def add_numbers(a, b):
        return a + b

    @staticmethod
    def multiply_numbers(a, b):
        return a * b

# Calling static methods
print("MathUtils Examples:")
result1 = MathUtils.add_numbers(5, 3)
print(f"5 + 3 = {result1}")

result2 = MathUtils.multiply_numbers(4, 2)
print(f"4 * 2 = {result2}")
print()

# Static Method for Utility Functions
class StringHelper:
    @staticmethod
    def is_palindrome(text):
        cleaned = ''.join(c.lower() for c in text if c.isalnum())
        return cleaned == cleaned[::-1]

    @staticmethod
    def count_words(text):
        return len(text.split())

print("StringHelper Examples:")
print(f"Is 'A man, a plan, a canal: Panama' a palindrome? {StringHelper.is_palindrome('A man, a plan, a canal: Panama')}")
print(f"Word count in 'Hello world from Python': {StringHelper.count_words('Hello world from Python')}")
print()

# Static Method in a Class with Instance Methods
class TemperatureConverter:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

print("TemperatureConverter Examples:")
# Instance method usage
converter = TemperatureConverter(25)
print(f"25°C in Fahrenheit (instance method): {converter.to_fahrenheit()}°F")

# Static method usage
print(f"25°C in Fahrenheit (static method): {TemperatureConverter.celsius_to_fahrenheit(25)}°F")
print(f"77°F in Celsius: {TemperatureConverter.fahrenheit_to_celsius(77)}°C")
print()

# Static Method for Validation
class UserValidator:
    @staticmethod
    def is_valid_email(email):
        return '@' in email and '.' in email.split('@')[1]

    @staticmethod
    def is_valid_password(password):
        return len(password) >= 8 and any(c.isdigit() for c in password)

print("UserValidator Examples:")
print(f"Is 'user@example.com' a valid email? {UserValidator.is_valid_email('user@example.com')}")
print(f"Is 'password123' a valid password? {UserValidator.is_valid_password('password123')}")
print(f"Is 'short' a valid password? {UserValidator.is_valid_password('short')}")

