import time
from math import sqrt
def fib(x):
	arr = [0 ,1, 2, 3]

	for i in range (4, x):
		add_num = arr[i-1] + arr[i-2]
		arr.append(add_num)

	print(*arr, sep = "\n")
	
#O(2^n)
def fib2(x):
	if x == 0:
		return 0
	elif x == 1:
		return 1
	else:
		return fib2(x-1) + fib2(x-2)

#wiki
def fib3(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))


sTime = time.time()
print('\n\n')


fib(35)
#print(fib3(30))


run_time =  round( (time.time() - sTime), 8)
print("--- %s seconds ---" % run_time)
print("\n\n")