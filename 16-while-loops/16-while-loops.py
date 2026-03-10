# 16-while-loops
# Python learning exercise

#while loops are used to execute a block of code repeatedly as long as a certain condition is true. 
# The syntax for a while loop is:

# Example 1: Basic while loop
count = 0
while count < 5:
    print("Count is:", count)
    count += 1  

# Example 2: Using while loop with user input
user_input = ""
while user_input.lower() != "exit":
    user_input = input("Type 'exit' to stop the loop: ")
    print("You entered:", user_input)

