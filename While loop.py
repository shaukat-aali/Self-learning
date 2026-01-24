#while loop= execute some code WHILE some condition remains true

'''name=input("Enter your name :")
while name=="":
    print("You did not enter your name")
    name=input("Enter your name :")
print(f"Hello {name}")'''

"""age=int (input("Enter your age :"))
while age<=0:
    print("Enter age cant be negetive")
    age=int(input("Enter your age :"))
print(f"You are {age} years old ") """

"""food= input("Enter the food you like :")
while not food== "":
    print("Please enter the food name ")
    food= input("Enter the food you like :")
print(f"The food you like is {food}")"""

num=int(input("Enter a number between 1 and 10 :"))
while num < 1 or num > 10:
    print("Please Eneter the number witin 1 and 10!")
    num=int(input("Enter a number between 1 and 10 :"))
print(f"The number you chose between 1 and 10 is :{num}")