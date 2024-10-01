# Variable is a name given to a memory location in a program
a = 2  # Data type - int (Integer)
b = "Tamanna"  # Data type - str (String)
c = 20.0  # Data type - float (Float)
d = None  # Data type - None
e = False  # Data type - bool (Boolean)

print(a)
print(b)
print(c)
print(d)
print(e)

# To check the data type of any variable we use type()
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# Operators are special symbols which perform operations on operands
# Arithmetic operators are those which perform mathematical operations (+, -, *, /, //, **)
x = 45
y = 56
z = 34

print(x + y)
print(y - z)
print(x * y)
print(x / y)  # always returns float value
print(x // y)  # floor division also returns integer value
print(x ** y)  # It will return x raised to the power y

# Relational operators are used to compare (<, >, <=, >=, == (equal to), != (not equal to), these operators always return answer in true or false)
print(x < y)
print(y > z)
print(x == y)
print(x != y)
print(x <= z)  # less than or equal to
print(x >= y)  # greater than or equal to

# Assignment operators used to assign values to variables (=, +=, -=, *=, /=)
num = 3
num += 6
print(num)
num -= 5
print(num)
num *= 4
print(num)

# Logical operators (and, or, not)
'''In case of and
true and true - true
false and false - false
true and false - false
false and true - false'''
print(3 < 4 and 7 > 8)
print(5 > 6 and 5 < 6)

'''In case of not
not true - false
not false - true'''
print(not 5 > 6)
print(not 6 < 8)

'''In case of or
true or true - true
false or false - false
true or false - true
false or true - true'''
print(45 < 45 or 56 < 89)

# Type conversion is basically the conversion of data type from one data type to another automatically by an interpreter
a = 2
b = 3.0
print(a + b)  # here 2 will be converted to 2.0 automatically by an interpreter because float data type is considered to be superior as compared to integer

x = "20"
y = 20
# print(x + y)  # will throw type error as we are adding string to integer

# To get its output we have to change string to integer and for that we have to use type casting in which data type is manually converted
x = int("20")
y = 20
print(x + y)  # now we will get output

# One very important point
# print(type(int("coder")))  # will throw value error we cannot convert sequence of characters to integer by type casting

# input function is used to accept the value from user and until and unless we use type casting
name = input("enter your name: ")
num = input("enter a number: ")  # it will be a string to make it int use type casting
num = int(input("enter a number: "))

# Mistakes and Refactoring:
# 1. Fixed indentation and spacing issues.
# 2. Corrected comments for better readability.
# 3. Removed incorrect type conversion example.
 