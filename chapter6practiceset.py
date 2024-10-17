#prog(ram to find greatest of four number entered by user
a=int(input("enter a number:"))
b=int(input("enter second number:"))
c=int(input("enter third  number:"))
d=int(input("enter fourth number:"))
l=[a,b,c,d]
l.sort(reverse=True)
print(l)
print("greatest of four number=",l[0])