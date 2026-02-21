# 7-if-staements
# Python learning exercise
passed_class = True

#simple boolean conditional statement

if passed_class:
    print("You passed the class!")
else:
    print("You unfortunately did not pass")

# numerical comparisons
# item1 == item2, item1 != item2, item1 < item2, item1 > item2, item1 <= item2, item1 >= item2

temperature_farenheit = 17
if temperature_farenheit < 32:
    print("It's freezing outside!")
else:
    print("It's not freezing outside!")

cost=29.95
if cost < 20:
    print("This is a good deal!")
else:
    print("This is not a good deal!")

#string comparisons
name = "Alice"
if name == "Alice":
    print("Hello, Alice!")
else:
    print("Hello, stranger!")

#other common string comparisons include !=, <, >, <=, >=
#these comparisons are based on the lexicographical order of the strings
word1 = "apple"
word2 = "banana"
if word1 < word2:
    print(f"{word1} comes before {word2} in the alphabet.")
else:    
    print(f"{word2} comes before {word1} in the alphabet.")

#null check is the most common use of if statements in programming. It is used to check if a variable is None (null) or not.
user_input = None

if user_input is None:
    print("No input provided.")
else:
    print(f"User input: {user_input}")

#date and time comparisons
from datetime import datetime

current_time = datetime.now()
if current_time.hour < 12:
    print("Good morning!")
else:
    print("Good afternoon!")

#checking for date is in past or future
from datetime import datetime

event_date = datetime(2024, 12, 25)  # Christmas
current_date = datetime.now()
if event_date > current_date:
    print("The event is in the future.")
else:
    print("The event is in the past.")


#demonstrate else if statements
score = 85
if score >= 90:
    print("You got an A!")
elif score >= 80:
    print("You got a B!")
elif score >= 70:
    print("You got a C!")
elif score >= 60:
    print("You got a D!")
else:
    print("You got an F!")

# In most cases we focuse on what we must do, then eliminate the scenarios where we do not need to do anything via an else statement. 
# We don't want to check for every possible scenario, we just want to check for the scenarios where we need to do something. 
# This is a common pattern in programming and is often referred to as "guard clauses"

#In some cases, we check for what must fail and nothing else. This will be mentioned later in this course
#when we talk about functions.