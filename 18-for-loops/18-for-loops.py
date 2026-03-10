# 18-for-loops
# Python learning exercise
# For loops are generally used when you know the number of iterations in advance, 
# while while loops are more flexible and can be used 
# when the number of iterations is not known beforehand.

for i in range(5):
    print("For loop iteration:", i)

#other for loop example
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("I like", fruit)

#for loop with break statement
for i in range(10):
    if i == 5:
        print("Breaking the loop at i =", i)
        break
    print("Current value of i:", i)

#use of continue statement in for loop
for i in range(10):
    if i % 2 == 0:
        continue  # Skip the rest of the loop for even numbers
    print("Current value of i (odd):", i)