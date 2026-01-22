#logical operators= evaluate multiple condition
#(or= at least one condition,and=both condition, not=not flase not true)

temp=20
is_raining=True

if temp>35 and is_raining:
  print("The event is cancelled")
  print("It is Cloudy")
elif temp<10 and not is_raining:
    print("THe event is cancelled")
    print("It is Cloudy")
elif temp<10 and  is_raining:
    print("THe event is onnn")
    print("It is Cloudy")
else:
 print("The event is onnnn")
    
 