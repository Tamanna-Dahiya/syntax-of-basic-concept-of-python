''' RAM -Random access memory which is volatile and once you terminates your program your data get lost
to persist data forever we use files'''
'''File is just data stored on storage device.There are two types of file one is text(.txt,.c) can be opened in notepad
and other is binary file (.jpg,.dat) ,python files on which we are working is text file'''
# In python there are so many function through which we can update,read or write in file.To open file we use open() function
# to open file we are supposed to provide two parameters one is file name and other is mode for opening file,if you don't provide node by default read mode
# let's write a program to read from file you can call read function only once
f.open("files.py","r")
data=f.read()
print(data)
f.close()# it is very important to close the file
# we can specify number of characters you want to read from file
f.open("files.py")
data=f.read(3)
print(data)
f.close()
# we use readline() of we want to read line of file and we can call this function as many time as you want
f.open("files.py")
data=f.readline()
print(data)

'''There are other modes also to open file like a for appending.t for updating,w for writing.one important thing is when you work in binary files then read mode will be specified as"rb", in text files is mode actually given as"rt"t comes by default if you don't give'''
#  for writing  content in files we use write or we can use append mode
f.open("files.py","w")
f.write("i am coder")
f.close()
# the best statement is with because by using that there is no need to close file
with open("files.py") as f :
    data=f.read()
    print(data)

    

