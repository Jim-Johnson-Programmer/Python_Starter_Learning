# 25-dictionaries
# Python learning exercise

# Dictionary structure is key and value pairs
# Example: {"key": "value"}

# Create a dictionary to store information about a person
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing values in a dictionary
print(person["name"])  # Output: Alice
print(person["age"])   # Output: 30
print(person["city"])  # Output: New York

# Adding a new key-value pair to the dictionary
person["profession"] = "Engineer"
print(person)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'profession': 'Engineer'}

# Updating an existing value in the dictionary
person["age"] = 31
print(person)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'profession': 'Engineer'}

# like the other collections, we can loop through a dictionary
# it is recommended to loop through the keys of the dictionary, 
# but we can also loop through the values or key-value pairs
for key in person:
    print(f"{key}: {person[key]}")

# Output:
# name: Alice
# age: 31
# city: New York
# profession: Engineer

