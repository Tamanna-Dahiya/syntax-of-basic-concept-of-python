# Creating A
for i in range (7):
    for j in range (5):
        if((j==0 or j==4)and i!=0 ) or ((i==0 or i==3) and (j>0 and j<4)):
            print("*",end="")
        else:
            print(end=" ") 
    print()  
# Creating B 
for i in range (7):
    for j in range (5):
        if(j==0 or j==4) or ((i==0 or i==3 or i==6) and (j>0 and j<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()
# Creating C 
for i in range (7):
    for j in range(5):
        if((j==0) and i in range (1,6)) or ((i==0 or i==6) and (j>0 and j<5)):
            print("*",end="")
        else:
            print(end=" ")
    print()                       
# Creating D 
for i in range (7):
    for j in range (5):
        if (j==0) or (j==4 and (i!=0 or i!=6)) or ((i==0 or i==6) and (j>0 and j<4)):
            print("*",end="") 
        else:
            print(end=" ") 
    print() 
# Creating E
for i in range(7):
    for j in range (5):
        if (j==0) or ((i==0 or i==3 or i==6) and (j>0 and j<=4)):
            print("*",end="")
        else:
            print(end=" ")
    print() 
# creating F 
for i in range(7):
    for j in range (5):
        if (j==0) or ((i==0 or i==3) and (j>0 and j<=4)):
            print("*",end="")
        else:
            print(end=" ")
    print()
# creating G
for i in range(6):
    for j in range(7):
        if (j==0) or ((i==0 or i==6) and (j>=0 and j<5)) or ((i==3) and (j>2 and j<6)) or ((i==4 or i==5) and (j==4)):
            print("*", end="")
        else:
            print(end=" ")
    print()                        
# creating H 
for i in range (7):
    for j in range (5):
        if (j==0 or j==4) or ((i==3) and j>0 and j<=4 ):
            print("*",end="")
        else:
            print(end=" ")
    print() 
#creating I
for i in range (6):
    print("*")
# creating j
for i in range (6):
    for j in range (5):
        if (j==2) or (i==0 and (j>=0 and j<5)) or (i==5 and (j>=0 and j<3)):
            print("*",end="")
        else:
            print(end=" ") 
    print()
# creating k
for i in range (7):
    for j in range (5):
        if (j==0) or ((i==3) and (j<=0 and j<2)) or ((i==2) and (j==2)) or ((i==1) and (j==3)) or ((i==0) and (j==4)) or ((i==4) and (j==2)) or ((i==5) and (j==3)) or ((i==6) and (j==4)):
            print("*",end="") 
        else:
            print(end=" ") 
    print() 
# creating L
for i in range (6):
    for j in range (5):
        if (j==0) or ((i==5) and (j>=0 and j<5)):
            print("*",end="") 
        else:
            print(end=" ") 
    print() 
# creating M
for i in range (7):
    for j in range(7):
        if (j==0 or j==6) or ((i==3) and(j==3)) or ((i==2) and (j==2 or j==4)) or ((i==1) and (j==1 or j==5)):
            print("*",end="")
        else:
            print(end=" ")
    print() 
# creating N
for i in range(7):
    for j in range(7):
        if (j==0 or j==6) or (i==1 and j==1)or (i==2 and j==2) or (i==3 and j==3) or (i==4 and j==4) or (i==5 and j==5):
            print("*",end="")
        else:
            print(end=" ")
    print()  
# creating O
for i in range(7):
    for j in range(5):
        if ((j==0 or j==4) and (i>0 and i<6)) or ((i==0) and (j>0 and j<4)) or ((i==6) and (j>0 and j<4)):
            print("*",end="")
        else:
            print(end=" ")
    print() 
# creating P
for i in range(7):
    for j in range(5):
        if ((j==0) and (i>0 and i<7)) or ((j==4) and (i>0 and i<3)) or ((i==0 or i==3) and (j<0 and j<4)) :
            print("*",end="")
        else:
            print(end=" ")  
    print()
# Creating Q
for i in range (8):
    for j in range(5):
        if ((j==0 or j==4) and (i>0 and i<6)) or ((i==0 or i==6) and (j>0 and j<4)) or ((i==5) and (j==1)) or((i==7) and (j==3)):
            print("*",end="")
        else:
            print(end=" ")
    print() 
# creating R
for i in range (7):
    for j in range (5):
        if (j==0) or ((i==0 or i==3) and (j>=0 and j<4)) or (( i==1 or i==2) and (j==4)) or ((j==4) and (i>3 and i<7)) :
            print("*",end="")
        else:
            print(end=" ")
    print() 
# creating S 
for i in range(7):
    for j in range(5):
        if ((i==0 or i==3 or i==6) and (j>0 and j<4)) or((j==0) and (i==1 or i==2)) or ((j==4) and(i==4 or i==5)):
            print("*",end="")
        else:
            print(end=" ")
    print()        
# creating T
for i in range (6):
    for j in range (5):
        if (j==2) or (i==0):
            print("*",end="")
        else:
            print(end=" ")
    print()
# Craeting U
for i in range (7):
    for j in range (5):
        if ((j==0 or j==4) and (i<+0 and i<6)) or ((i==6) and (j<0 and j<4)):
            print("*",end="")
        else:
            print(end =" ")
    print()
# creating V 
for i in range (4):
    for j in range(7):
        if ((i==0) and (j==0 or j==6)) or ((i==1) and (j==1 or j==5)) or ((i==2) and (j==2 or j==4)) or ((i==3) and (j==3) ):
            print("*",end="") 
        else:
            print(end=" ")
    print()
# creating W
for i in range(5):
    for j in range(5):
        if (j==0 or j==4 ) or ((i==3) and(j==1 or j==3)) or ((i==2) and (j==2)):
            print("*", end="")
        else:
            print(end=" ")    
    print() 
# creating X
for i in range(5):
    for j in range (5):
        if ((j==0 or j==4) and (i==0 or i==4)) or ((j==1 or j==3) and (i==1 or i==3)) or (j==2 and i==2):
            print("*",end="")
        else:
            print(end=" ")
    print() 
# creating Y 
for i in range (5):
    for j in range(5):
        if ((i==0) and (j==0 or j==4)) or ((i==1) and (j==1 or j==3)) or ((j==2) and (i>1 and i<5)):
            print("*",end="")
        else:
            print(end=" ")
    print()
# creating Z 
for i in range (4):
    for j in range (4):
        if (i==0 or i==3) or((i==1) and (j==2)) or ((i==2) and (j==1)) :
            print("*",end="")
        else:
            print(end=" ")
    print() 
s