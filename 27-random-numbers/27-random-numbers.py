# 27-random-numbers
# Python learning exercise

import random

# Generate a random integer between 1 and 100
random_number = random.randint(1, 100)
print(f"Generated random number: {random_number}")
# Generate a random float between 0 and 1
random_float = random.random()
print(f"Generated random float: {random_float}")
# Generate a random choice from a list
choices = ['apple', 'banana', 'cherry', 'date']
random_choice = random.choice(choices)
print(f"Randomly chosen fruit: {random_choice}")
# Generate a random sample of 3 unique numbers from a range of 1 to 10
random_sample = random.sample(range(1, 11), 3)
print(f"Random sample of 3 unique numbers from 1 to 10: {random_sample}")
