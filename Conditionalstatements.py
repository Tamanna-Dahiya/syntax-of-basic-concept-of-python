# conditional statements are those statements which are executed when the condition sets to be true
''' For example, if I say if the day is sunny I am going to order an ice cream, so this task is possible only if the condition is true.
Similarly, in Python programming, there are some statements which will only execute if the condition sets to be true.'''

# Simple syntax of if-else
a = 3
b = 6
c = 9

if a < b:  # In this code, if the condition of if is true, then the statement of if will be executed, and if the condition of if is false, then the statement of else will be executed.
    print("a is lesser than b")
else:
    print("a is greater than b")

# if-elif-else
if a > b:
    print("a is greater than b")
elif b < c:
    print("b is lesser than c")
else:
    print("none")

# One important tip - think of as many possibilities you can try to execute that will help you in understanding this concept
'''In if-elif-else ladder, first if the condition of if is true, then its statement is executed and the program will terminate.
If the condition is false, then the condition of elif will be checked. If it sets to true, that will be executed and the program terminates. If not, then it moves to else.'''

# Multiple if statements (multiple if statements will execute independently)
if a < b:
    print("a is lesser than b")
if a < c:
    print("a is lesser than c")
if b < c:
    print("b is lesser than c")
elif c < b:
    print("c is lesser than b")
else:
    print("ok")

# Multiple elif statements and it will not execute independently
if a < b:
    print("a is lesser than b")
elif b < c:
    print("b is lesser than c")
elif a < c:
    print("a is lesser than c")
elif c < a:
    print("c is lesser than a")
else:
    print("ok")

# Mistakes and Refactoring:
# 1. Fixed indentation issues.
# 2. Corrected comments for better readability.
# 3. Added missing elif condition in the last block.# conditional statements are those statements which are executed when the condition sets to be true
