# 23-2d-collections
# Python learning exercise

# 2D list (list of lists)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements
print(matrix[0][0])  # Output: 1
print(matrix[1][2])  # Output: 6
# Modifying elements
matrix[0][1] = 20
print(matrix)  # Output: [[1, 20, 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
    for element in row:
        print(element, end=' ')
    print()  # New line after each row  

