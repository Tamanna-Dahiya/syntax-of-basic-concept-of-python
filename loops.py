# Loops is used to repeat a set of instructions 
# By using loops it get easier for user to tell system which set of statements is to be repeated and how
# two most common types of loops are for and while loop
# syntax of while loop 
''' while condition :
        body of loop'''# body of loop will only execute if condition sets to be true
# program to print number from 1-10
i=1
while i<=10:
    print(i)
    i=i+1
# to print yes 5 times 
i=1
while i<6:
    print("yes")
    i=i+1
# to print a multiplication table of any number
num=int(input("enter a number:"))
i=1
while i<=10:
    print(num*i)
    i=i+1
# to print elements of list 
l=[1,2,3,4,5]
i=0
while i<len(l):
    print(l[i])
    i=i+1
# for loop
#for loop is used to iterate through sequence like list,tuple
# program to print numbers from 1-10
for i in range(1,11):#upper limit will be excluded
    print(i)        
# to print content of list using for loop
l=[1,2,3,4,5]
for i in l:
    print(i)
# to print table of any number using for loop
num=int(input("enter a number"))
for i in range (1,11):
    print(num*i)
# to print table of any number in reverse order
num=int(input("enter a number:"))
for i in range (10,0):
    print(num*i)
# break statement
for i in range(5):
    if i==2:
        break
    print(i)
#continue statement
for i in range (5):
    if i==2:
        continue
    print(i)
# pass statement
for i in range (4):
    if i==3:
        pass
    print(i)            
