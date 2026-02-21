# 3-ask-type-casting
# Python learning exercise
first_name = "Jim"
print(f"Hello {first_name}")

student_count = 20
print(f"Our class has {student_count} students")

distance = 1.5
print(f"I jogged {distance} miles")

# how to get datatype given to you for when variable is not assigned or casted
x = 42
print(type(x))

x = 3.14
print(isinstance(x, float))     # True

#return true if ANY of types in tuple passed in
print(isinstance(x, (int, float)))  # True

