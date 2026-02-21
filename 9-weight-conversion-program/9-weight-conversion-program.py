# 9-weight-conversion-program
# Python learning exercise

print("Welcome to the Weight Conversion Program!")
print("Please select the conversion you want to perform:")
print("1. Kilograms to Pounds")
print("2. Pounds to Kilograms")
conversion_choice = input("Enter the number corresponding to the conversion (1/2): ")
if conversion_choice == '1':
    weight_kg = float(input("Enter the weight in kilograms: "))
    weight_lb = weight_kg * 2.20462
    print(f"{weight_kg} kg is equal to {weight_lb:.2f} lb.")
elif conversion_choice == '2':
    weight_lb = float(input("Enter the weight in pounds: "))
    weight_kg = weight_lb / 2.20462
    print(f"{weight_lb} lb is equal to {weight_kg:.2f} kg.")
else:
    print("Invalid conversion selected. Please choose a valid conversion (1/2).")
    