#type casting : converting a variable from one data type to another eg: str(),int(),flaot().bool()
name="Shaukat Taufique Aali"
age=23
gpa="3"
is_student=True

print(type(age))
#Output 'int'
age = str(age)
print(type(age))
#new output for age "<class 'str'>"

age+= "1"
print(age)
#output as string 231 else for int error.