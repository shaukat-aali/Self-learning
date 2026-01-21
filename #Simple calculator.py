#Simple calculator
import math
A=int(input("Enter Number 1 :"))
Ari=input("Enter Arthmatic opperation (+,-,*,/) :")
B=int(input("Enter Number 2 :"))
if Ari=="+":
    sum=A+B
    print(f"Adding Number {A} AND {B} :{sum}")
elif Ari=="-":
    sum=A-B
    print(f"Subtracting {A} AND {B}  :{sum}")
elif Ari=="*":
    sum=A*B
    print(f"Multipling {A} AND {B} :{sum}")
elif Ari=="/":
    sum=A/B
    print(f"Deviding {A} AND {B} :{sum}")
else:
    print("Wrong input")