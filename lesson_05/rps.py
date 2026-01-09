###Rock paper scissors game###

# value = input("Please enter a value")

# print("You entered: " + value)

###Move terminal window to right side to create column next to column layout###
###View -> Appearance -> Move Primary Side Bar to Right###
###############################################################
# import random
# import sys
RPSChoices

# print("")
# player_choice = input("Enter your choice...\n1 for rock \n2 for paper \n3 for scissors\n\n")

# ###string is safest type for user input, why?###
# player_choice_cast = int(player_choice)

# ##validate player choice and assign name, use exclustion logic to say, limited choices are valid, anything else is invalid
# if player_choice_cast < 1 or player_choice_cast > 3:
#     print("Invalid input! Please enter a number between 1 and 3.")
#     sys.exit()


# computer_choice = random.choice("123")
# computer = int(computer_choice)

# # computer_choice = random.randint(1, 3)


# print("Player chose: " + player_choice)
# print("Computer chose: " + str(computer))

# #determine winner
# if player_choice_cast == computer:
#     print("It's a tie!")
#     # rock beats scissors or paper beats rock or scissors beats paper
# elif (player_choice_cast == 1 and computer == 3) or \
#     (player_choice_cast == 2 and computer == 1) or \
#     (player_choice_cast == 3 and computer == 2):     
#     print(" 😊 Player wins!")
# else:
#     print(" 💻 Computer wins!")

###################################################################
#enums make code more readable, also can use constants
#ROCK = 1
#PAPER = 2
#SCISSORS = 3

import random
import sys
from enum import Enum

# # #not updateable enum class for RPS choices
class (Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

# print(RPSChoices(2))
# print(RPSChoices.ROCK)
# print(RPSChoices.ROCK.name)
# print(RPSChoices.ROCK.value)
# print(RPSChoices['ROCK'])
# print(type(RPSChoices.ROCK))

print("")
player_choice = input("Enter your choice...\n1 for rock \n2 for paper \n3 for scissors\n\n")

###string is safest type for user input, why?###
player_choice_cast = int(player_choice)

##validate player choice and assign name, use exclustion logic to say, limited choices are valid, anything else is invalid
if player_choice_cast < 1 or player_choice_cast > 3:
    print("Invalid input! Please enter a number between 1 and 3.")
    sys.exit()


computer_choice = random.choice("123")
#computer_choice = random.randint(1, 3)
computer = int(computer_choice)

print("Player chose: " + str(RPSChoices(player_choice_cast)).replace("RPSChoices.",""))
print("Computer chose: " + str(RPSChoices(computer)).replace("RPSChoices.",""))

#determine winner
if player_choice_cast == computer:
    print("It's a tie!")
    # rock beats scissors or paper beats rock or scissors beats paper
elif (player_choice_cast == 1 and computer == 3) or \
    (player_choice_cast == 2 and computer == 1) or \
    (player_choice_cast == 3 and computer == 2):     
    print(" 😊 Player wins!")
else:
    print(" 💻 Computer wins!")