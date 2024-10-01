# String is a built-in data type that stores a sequence of characters. The sequence of characters is enclosed within single, double, or triple quotes.
# To swap multiline string always use single triple quotes, and if you are using an apostrophe in a string then do not use single quotes
a = "coder"  # string
b = 'coder'  # string
c = '''coder'''  # string

# Corrected multiline string usage
print('''twinkle twinkle little star
      how I wonder what you are''')

# Corrected usage of quotes with apostrophe
print("my father's")

# Concatenation is an operation to add two or more strings
name = input("enter your name: ")
print("good morning " + name)

# len() - it is a function to retrieve the number of characters in a string
x = "coder"
print(len(x))

# Indexing - it is used to retrieve a character from a string
x = "Tamanna Dahiya"  # consider space as one character
print(x[0])
print(x[1])

# Removed incorrect assignment to immutable string
# x[1] = "h"  # throws type error as string is an immutable data type

# Slicing - It is used to fetch a part of a string
x = "Tamanna Dahiya"  # consider space as one character
print(x[1:4])  # will exclude upper limit

# Some other functions let's first discuss endswith
print(x.endswith("ya"))  # returns answer either true or false

# capitalize() - will convert the first letter to uppercase
x = "tamanna Dahiya"  # consider space as one character
print(x.capitalize())

# replace() - will replace a character in the string with another character
print(x.replace("a", "c"))

# find() - will retrieve the index of the given character of the first occurrence
print(x.find("a"))

# count() - will tell the number of times a character comes in a string
print(x.count("a"))

# Escape sequence characters starting with backslash followed by one or more characters generally used for formatting
# \a - beep sound
# \n - new line
# \t - tab space
# \a, \n, \t considered to be single characters

# Mistakes and Refactoring:
# 1. Fixed multiline string and apostrophe usage.
# 2. Removed incorrect assignment to immutable string.
# 3. Improved readability and consistency in comments.
