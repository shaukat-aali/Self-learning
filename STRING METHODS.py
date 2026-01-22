#STRING METHODS

#name=input("Enter your full name :")
#result=len(name)
#result=name.find(" ")# for finding first interation
#result=name.rfind(" ")#for finding last iteration
#name=name.upper()#upper case
#name=name.lower()#lower case
#name=name.isdigit()# returns boolean only for digits no alphabet 
#name=name.isalpha()#returns boolean only for alphabet
#name=name.count("a")
#name=name.replace("a","A")
#print (name)

#print(help(str)) help with python dicitornary

username=input("Enter your new username:")
if len(username)>12:
    print("username too big fit within 12 charectors")
elif not username.find(" ") == -1:
    print("Username should not contain spaces")
elif username.isalpha == False:
    print("The username should not contain digits")
else:
    print(f"Welcome {username}")