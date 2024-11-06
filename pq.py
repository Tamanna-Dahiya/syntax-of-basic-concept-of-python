# 1st question(square pattern)
n=int(input ("enter a number:")) 
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()    
# increasing triangle
n=int(input ("enter a number:")) 
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
# decreasing triangle
n = int(input("enter a number:"))
for i in range (n):
    for j in range (i,n):
        print("*",end=" ") 
    print() 
# increasing right angled triangle 
n= int(input("enter a number:"))
for i in range (n):
    for j in range (i,n):
        print(" ",end=" ")
    for j in range (i+1):
        print("*",end=" ")
    print() 
# decreasing right angle 
n=int(input("enter any number:"))
for i in range(n):
    for j in range (i+1):
        print(" ",end=" ")
    for j in range (i,n):
        print("*",end=" ")
    print() 
# upper pyramid 
n=int(input("enter a number:")) 
for i in range (n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range (i):
        print("*",end=" ")
    for j in range (i+1):
        print("*",end=" ")
    print()
# lower pyramid 
n=int(input("enter a number:"))
for i in range (n):
    for j in range (i+1):
        print(" ",end=" ")
    for j in range (i,n-1):
        print("*",end=" ")
    for j in range (i,n):
        print("*",end=" ")
    print()            
# diamond pattern  
n= int(input("enter a number:"))
for i in range(n):
    for j in range (i,n):
        print(" ",end=" ")
    for j in range (i):
        print("*",end=" ")
    for j in range (i+1):
        print("*",end=" ")
    print()
for i in range (n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range (i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()                
