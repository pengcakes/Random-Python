#converts any amount of minutes to hours and minutes

def TimeConvert(num):
	minutes = num%60
	hours = int(num/60)
	print(f"{hours}:{minutes}")
	return None 

TimeConvert(24*60)


#modulus returns leftover
#to round down parse to int
# can use f to format string in python 3+