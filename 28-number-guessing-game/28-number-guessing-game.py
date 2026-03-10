# 28-number-guessing-game
# Python learning exercise

import random

print("Welcome to the Number Guessing Game!")

min_range = input("Enter the minimum number for the range: ")
max_range = input("Enter the maximum number for the range: ")

try:
    min_num = int(min_range)
    max_num = int(max_range)
    if min_num >= max_num:
        print("Minimum must be less than maximum.")
        exit()
except ValueError:
    print("Please enter valid integers.")
    exit()

secret_number = random.randint(min_num, max_num)
guesses = 0

while True:
    guess = input(f"Guess a number between {min_num} and {max_num}: ")
    try:
        guess_num = int(guess)
        guesses += 1
        if guess_num < min_num or guess_num > max_num:
            print(f"Please guess within the range {min_num} to {max_num}.")
            continue
        if guess_num < secret_number:
            print("Too low!")
        elif guess_num > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed it in {guesses} guesses.")
            break
    except ValueError:
        print("Please enter a valid number.")

