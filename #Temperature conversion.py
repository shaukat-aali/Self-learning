#Temperature conversion
units = {"1": "Celsius",    "2": "Fahrenheit","3": "Kelvin"}
print("Temperature Units:")
for key, value in units.items():
    print(f"{key}. {value}")
choice = input("Enter the unit you want to convert: ")
if choice in units:
    selected = units.pop(choice)
else:
    print("Invalid choice")
    exit()
print(f"\nConvert {selected} to:")
for key, value in units.items():
    print(f"{key}. {value}")

Temp2 = input("Enter the option number: ")
Unit=int(input("Enter the units to be converted :"))
if choice=="1" or Temp2 =="2":
    temp=Unit*(9/5)+32
    print(f"{Unit} Celsius = {temp} Fahrenheit")
elif choice=="2" or Temp2=="1":
    temp=(Unit-32)*(5/9)
    print(f"{Unit} Fahrenheit = {temp} Celsius")
elif choice=="1" or Temp2=="3":
    temp=Unit+273.15
    print(f"{Unit} Celsius = {temp} Kelvin")
elif choice=="3" or Temp2=="1":
    temp=Unit-273.15
    print(f"{Unit} Kelvin = {temp} Celsius")
elif choice=="2" or Temp2=="3":
    temp=(Unit-32)*(5/9)+273.15
    print(f"{Unit} Fahrenheit = {temp} Kelvin")
elif choice=="3" or Temp2=="2":
    temp=(Unit-273.15)*(9/5)+32
    print(f"{Unit} Kelvin = {temp} Fahrenheit")


