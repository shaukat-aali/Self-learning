#String indexing
#indexing means accesing element at certaion position using 
#[] i.e indexing operator ( starting index : ending index)

phone_num= "3425353634636"
#print(phone_num[1],phone_num[2])
#print(phone_num[0:6])
#print(phone_num[:6]) #will give samew result
#print(phone_num[-4:]) # -index for reverse
#print(phone_num[::2])
phone_num=phone_num[::-1]
print(phone_num)