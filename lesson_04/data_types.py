##help(str) #get help on string methods and attributes
## https://docs.python.org/  drop down at top should get set to 3.13.11, click on Library Reference, then click on Text Processing Services, string -- Common Sting Operations

# first = "Jim"
# last = "Johnson"

# print(type(first)) #reveal the type of the variable
# print(type(first) == str) #check if the type is string
# print(isinstance(first, str)) #check if the variable is an instance of string

# pizza = str("Pepperoni") #create a string using the str() constructor
# print(type(pizza)) #reveal the type of the variable
# print(type(pizza) == str) #check if the type is string
# print(isinstance(pizza, str)) #check if the variable is an instance of string

## concatenation
# full_name_statement = "Hello " + first + " " + last
# ##first example from string.format() method
# full_name_statement = "Hello {} {}".format(first, last)
# full_name_statement = f"Hello {first} {last}"
# print(full_name_statement) #print the full name

# ## multiline strings
# ### using triple double quotes
# multipline_lines = """This is line one
# This is line two  
# This is line three"""
# print(multipline_lines)

### using triple single quotes, is more problematic when using apostrophes
# single_line_string = "This is a single line string with an apostrophe: Jim's I'm learning Python."
# print(single_line_string)
# multipline_lines = '''This is line one
# This is line two  
# This is line three'''
# print(multipline_lines)

## special characters
### using escape sequences for new line \n and tab \t
# special_characters = 'I\'m learning\nPython\tProgramming'
# special_characters = "I'm learning\nPython\tProgramming"
# print(special_characters)

### using raw strings to ignore escape sequences
# raw_string = r"C:\Users\Jim\Documents\Python"
# print(raw_string) #prints the raw string without interpreting escape sequences
# double_backslash = 'C:\\Users\\Jim\\Documents\\Python'
# // forward slash = r"C:/Users/Jim/Documents/Python"
# \\ backshlash = r"C:\\Users\\Jim\\Documents\\Python"
# escape characters = 'C:\\\\Users\\\\Jim\\\\Documents\\\\Python'
# print(double_backslash) #prints the string with double backslashes interpreted as single backslashes


## string methods
sample_string = "  Hello, World! Welcome to Python Programming.  "
# 
# print(len(sample_string)) #get original length of the string
# print(len(sample_string.strip())) #get length of the string after stripping whitespace

# print(sample_string.find("World")) #find the starting index of substring
# print("Programming word not found" if sample_string.find("World")>-1 else "Programming word found") #find the starting index of substring

# # print("Programming word not found" if sample_string.count("Programming")>-1 else "Programming word found") #count occurrences of substring
# # print(sample_string.count("o")) #count occurrences of substring

# print(sample_string.startswith("  Hello")) #check if string starts with substring
# print("Programming word not found" if sample_string.endswith("Programming") else "Programming word found") #check if string ends with substring

# print(sample_string.replace("World", "Universe")) #replace substring

# print(sample_string.split(" ")) #split string into a list by spaces

# print("")
# title = "menu".upper()
# print(title.center(20, '=')) #center the string with padding characters

# ##left justify and right justify
# print("Coffee".ljust(16, ".") + "$1".rjust(4)) #left justify with padding characters
# print("Tea".ljust(16, ".") + "$1".rjust(4)) #left justify with padding characters
# print("Sandwich".ljust(16, ".") + "$1".rjust(4)) #left justify with padding characters

## string index values
first = "Jim"
last = "Johnson"
# print(first[0]) #first character, zero based index
# print(first[1]) #second character
# print(last[-1]) #last character
# print(last[-2]) #second to last character

# ## string slicing with ranges
# print(first[0:2]) #characters from index 0 to 1, not including 2
# print(last[1:4]) #characters from index 1 to 3
# print(first[:3]) #characters from start to index 2
# print(first[2:]) #characters from index 2 to end
# print(first[:]) #entire string

# print(sample_string.strip().startswith("H")) #check if string starts with substring
# print("Programming word not found" if sample_string.strip().endswith("g") else "Programming word found") #check if string ends with substring

##casting
## Boolean
# first_bool_variable = True
# second_bool_variable = bool(False)
# print(type(first_bool_variable)) #boolean is True
# print(type(second_bool_variable)) #empty string is False
# print(isinstance(first_bool_variable, bool)) #check if the variable is an instance of boolean

## Numeric data types
### Integer
# price = 100
# best_price = int(90)
# print(type(price)) #integer type
# print(isinstance(price, int)) #integer type

# ### Float(decimal)
# discount = 19.99
# best_discount = float(15.99)
# print(type(discount)) #float type
# print(isinstance(discount, float)) #float type

# ### Complex
# complex_number = 2 + 3j #2 is real part, 3 is imaginary part
# print(type(complex_number)) #complex type
# print(isinstance(complex_number, complex)) #complex type
# print(complex_number.real) #real part
# print(complex_number.imag) #imaginary part

### Casting between numeric types
# integer_from_float = int(19.99) #truncates decimal part
# print(integer_from_float)
# float_from_integer = float(100) #adds decimal part
# print(float_from_integer)
