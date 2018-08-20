def fib(x):
	arr = [1, 2, 3]

	for i in range (3, x):
		add_num = arr[i-1] + arr[i-2]
		arr.append(add_num)

	print(*arr, sep = "\n")
	


fib(31)