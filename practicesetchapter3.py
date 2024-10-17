#program to display a user entered name followed by good afternoon using input()
 #name =input("enter your name:")
 #print("goodafternoon"+name)
#program to fill in letter template given below with name and date
 letter='''Dear <|name|>,
                you are selected!
                 <|Date|>'''
name =input("enter your name:")
Date=input("enter date:")
letter=letter.replace("<|name|>",name)
letter=letter.replace("<|Date|>",Date)
print(letter)