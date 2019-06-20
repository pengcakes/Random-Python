
"""
Alphanumeric w/ symbols on keyboard:
16=top row
16=ones on right side

(26 + 26 + 10 + 16 + 16) ^ 6 
= 689869781056 = 6.9E11

"""

import random

password = random.randint(10000000,99999999)
print("Password: ",password)


# brute force
def bf1(password):
	for x in range(10000000, 99999999):
		if(x==password):
			print("Ans: ", x)

# brute force but for each digit
# won't work... can't check each digit irl
def bf2(password):
	pass_chars=[int(x) for x in str(password)]
	ans=[]
	for x in pass_chars:
		for y in range(0,10):
			if(y==x):
				ans.append(y)
	print(ans)


"""
avg 0.048s for 4 num pass
real	0m0.049s
user	0m0.032s
sys	0m0.013s

avg 4.7-5.2s for 8 num pass
real	0m4.897s
user	0m4.792s
sys	0m0.040s


"""

#bf1(password)


"""
avg 0.050s for 4 num pass
real	0m0.050s
user	0m0.032s
sys	0m0.014s

avg 0.049s for 8 num pass
real	0m0.049s
user	0m0.031s
sys	0m0.014s
"""

bf2(password)



