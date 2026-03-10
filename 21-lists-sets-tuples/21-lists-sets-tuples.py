# 21-lists-sets-tuples
# Python learning exercise

# Lists []
# Lists are ordered, mutable, and can contain duplicate elements. They are defined using square brackets [].
my_list = [1, 2, 3, 4, 5]
print(my_list)

for item in my_list:
    print(item)

nested_list = [1, 2, [3, 4], 5]
print(nested_list)

for item in nested_list:
    if isinstance(item, list):
        for sub_item in item:
            print(sub_item)
    else:
        print(item)

# Sets {}
# Sets are unordered, mutable, and do NOT allow duplicate elements. 
my_set = {1, 2, 3, 4, 5}
print(my_set)

nested_set = {1, 2, {3, 4}, 5}
print(nested_set)


# Tuples ()
# Tuples are ordered, immutable, and can contain duplicate elements. They are defined using parentheses ().
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

nested_tuple = (1, 2, (3, 4), 5)
print(nested_tuple)