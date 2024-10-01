# Loops are used to repeat a set of instructions
# By using loops it gets easier for the user to tell the system which set of statements is to be repeated and how
# Two most common types of loops are for and while loop

# Syntax of while loop
''' while condition:
        body of loop'''  # body of loop will only execute if condition sets to be true

# Program to print numbers from 1-10
i = 1
while i <= 10:
    print(i)
    i = i + 1

# To print yes 5 times
i = 1
while i < 6:
    print("yes")
    i = i + 1

# To print a multiplication table of any number
num = int(input("enter a number: "))
i = 1
while i <= 10:
    print(num * i)
    i = i + 1

# To print elements of a list
l = [1, 2, 3, 4, 5]
i = 0
while i < len(l):
    print(l[i])
    i = i + 1

# For loop
# For loop is used to iterate through sequences like list, tuple

# Program to print numbers from 1-10
for i in range(1, 11):  # upper limit will be excluded
    print(i)

# To print content of list using for loop
l = [1, 2, 3, 4, 5]
for i in l:
    print(i)

# To print table of any number using for loop
num = int(input("enter a number: "))
for i in range(1, 11):
    print(num * i)

# To print table of any number in reverse order
num = int(input("enter a number: "))
for i in range(10, 0, -1):  # Added step to range for reverse order
    print(num * i)

# Break statement
for i in range(5):
    if i == 2:
        break
    print(i)

# Continue statement
for i in range(5):
    if i == 2:
        continue
    print(i)

# Pass statement
for i in range(4):
    if i == 3:
        pass
    print(i)
