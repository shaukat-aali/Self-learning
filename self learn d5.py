#if  statement :- it is used to put condition to a argument and if true proceed 
#if not use else condition.

#age=int (input("Enter your age :-"))
#if age>=18:
#    print("You are eligible to vote")
#elif age <=13:
#    print("You are not bourn yet") 
#else:
#    print("You are not eligible to vote")

response = input("Would you like food ?(Y/N))")
if response=="Y":
    print("What food would you like :")
    food=int (input("Here is the menu :-1.Burgurn 2.Pizza 3.Biriyani:-"))
    if food in (1,2,3):
     print(f"Food ordered:{food}") 
    else:
     print("Worng option")
else:
    print("What else would you like")    
