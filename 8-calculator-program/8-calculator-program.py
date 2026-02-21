# 8-calculator-program
# Python learning exercise

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))   
print("Select the operation you want to perform:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
operation = input("Enter the number corresponding to the operation (1/2/3/4): ")
if operation == '1':
    result = first_number + second_number
    print(f"The result of addition is: {result}")
elif operation == '2':
    result = first_number - second_number
    print(f"The result of subtraction is: {result}")
elif operation == '3':
    result = first_number * second_number
    print(f"The result of multiplication is: {result}")
elif operation == '4':    
    if second_number != 0:
        result = first_number / second_number
        print(f"The result of division is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation selected. Please choose a valid operation (1/2/3/4).")

