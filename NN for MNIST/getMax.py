
trial = 'res3'

with open('/Users/dustindeng/Google Drive/Code/NN/' + trial + '.txt') as r:
	lines = r.read().splitlines()

def findMax():
	maxV = max(lines)
	num = lines.index(maxV)

	print("#" + str(num) + " : " + maxV)

	lines.remove(maxV)


print("\nTop 3 of " + trial + ": \n")
findMax()
findMax()
findMax()
# print("max val: " + maxV)
# print("#: " + str(num))