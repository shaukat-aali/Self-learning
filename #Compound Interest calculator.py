#Compound Interest calculator

import math
P=0
r=0
T=0
while P<=0:
    P=float(input("Enter the Principal amount :"))  #Principal amount
    if P<=0:
        print("The entered amount is not valid") 
while r<=0:
    r=float(input("Enter the Rate of Interest :"))  #rate of Interest
    if r<=0:
        print("The entered Rate is not valid") 
while T<=0:
    T=float(input("Enter the Time (in Years) :"))   #time
    if T<=0:
        print("The entered Time is not valid") 
r=r/100
A=P*((1+r)**T) #Final amount
CI=A-P
print(f"The final ammount is :${round (A):,}")
print(f"The Compund Interest is :${round(CI):,}")