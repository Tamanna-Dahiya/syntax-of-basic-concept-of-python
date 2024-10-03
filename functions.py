#Functions are statements which performs a specific task
''' need of fumctions can be understand with the help of example is that bif we want to find sum of two numbers in a program so many times so rather
we can define function to find sum of two numbers
in short,functions imporve readability of code as well as reusability'''
# lets write a program to define a fucction to find sum of two numbers
def sum(a,b):# def is a keyword here used for defining a function(a,b is an argument here)
    return a+b
x=sum(3,5)#calling a function
print(x)
# let's write one more program to find average of 3 numbers
def avg(a,b,c):
    return (a+b+c)/3
y=avg(6,5,4)
print(y)
# what if you forget to pass arguments while calling a function so that will give error so to avoid this you can give default parameter
def sum(a=1,b=1)
    return a+b
x=sum()#calling a function
print(x)
# It is also possible if you pass only single argument as default 
def sum(a=1,b):
    return a+b
x=sum(3)
print(x)
# if we don't we give any parameter while defining a function or while calling a function then it will give none

