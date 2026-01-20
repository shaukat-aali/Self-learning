#input() = A function that prompts the user to enter data 
# returns the entered data as string.
Name=input("Enter your name:")
Age =input("What is your age?: ")

print(f"Your name is {Name}:")
print(f"Your age is: {Age}")
Age=int(Age)
Age=Age +1
print(f"Next year you will be:{Age}")

