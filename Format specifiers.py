#Format specifiers ={Value:flags}
# .(number)f	Round to that many decimal places (fixed point).
# :(number)	Allocate that many spaces.
# :0(number)	Allocate and zero pad that many spaces (e.g., :03).
# :< =	Left justify.
# :^ =	Center align.
# :+ =	Use a plus sign to indicate positive values.
# :=  =	Place sign to the leftmost position.
# :  = Insert a space before positive numbers.
# :, =	Comma separator (e.g., 1,000).
price1= 3.2456
price2= -5452312.56865
price3= 43.352
print(f"price1 is ${price1:<+,.2f}")
print(f"price1 is ${price2:,}") 
print(f"price1 is ${price3:^10}")