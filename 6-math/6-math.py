# 6-math
# Python learning exercise
# -------------------------------
# Python Math Operations Examples
# -------------------------------

import math

# Addition
print(5 + 3)        # 8

# Subtraction
print(10 - 4)       # 6

# Multiplication
print(7 * 6)        # 42

# True Division
print(8 / 3)        # 2.6666666666666665

# Floor Division
print(8 // 3)       # 2

# Modulus (remainder)
print(10 % 3)       # 1

# Exponentiation
print(2 ** 5)       # 32

# Unary Plus
x = 5
print(+x)           # 5

# Unary Minus
print(-x)           # -5

# Order of Operations (PEMDAS)
print(2 + 3 * 4)    # 14
print((2 + 3) * 4)  # 20

# Math with Floats
print(3.5 + 2.1)    # 5.6
print(5.0 * 2)      # 10.0

# Mixed Types (int + float → float)
print(5 + 2.5)      # 7.5

# Absolute Value
print(abs(-12))     # 12

# Power and Roots
print(pow(3, 4))    # 81
print(16 ** 0.5)    # 4.0

# Rounding
print(round(3.14159, 2))   # 3.14

# math module examples
print(math.sqrt(49))       # 7.0
print(math.factorial(5))   # 120
print(math.pi)             # 3.141592653589793
print(math.sin(math.pi/2)) # 1.0

# Comparison Operators
print(5 > 3)        # True
print(5 < 3)        # False
print(5 == 5)       # True
print(5 != 4)       # True
print(5 >= 5)       # True
print(3 <= 2)       # False

###########################################################
gallons_of_gasoline_integer = 5
gallons_of_gasoline_float = 5.31
price_per_gallon_integer=2


gallons_of_diesel_float = 8.25
price_per_gallon_float=2.85

cost_for_gas_integer = gallons_of_gasoline_integer * price_per_gallon_integer
print(type(cost_for_gas_integer))
print(f"gas cost was {cost_for_gas_integer}")

cost_for_diesel = gallons_of_diesel_float * price_per_gallon_float
print(type(cost_for_diesel))
print(f"gas cost was {cost_for_diesel}")

expected_exception = 234/0
