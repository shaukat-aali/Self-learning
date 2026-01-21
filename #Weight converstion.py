#Weight converstion

A=input("Enter enter the conversion unit :\n1.Pounds to Kilograms\n2.Kilograms to pounds:\n")
B=int(input("Enter the Quantity to coverte:"))
if A =="1" or A =="Pounds to Kilograms":
    Coversion=B*2.20462
    CoversionR=round(B*2.20462)
    print(f"Converting {B} Pounds to Kilograms:{Coversion}")
    print(f"Rounding{CoversionR}")
elif A =="2" or A =="Kilograms to pounds":
    Coversion=B*0.453592
    CoversionR=round(B*0.453592)
    print(f"Converting {B} Kilograms to Pounds we get :{Coversion}")
    print(f"Rounding:{CoversionR}")
else:
    print("Wrong input")