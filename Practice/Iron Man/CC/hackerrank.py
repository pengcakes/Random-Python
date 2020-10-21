def simpleArraySum(ar):
	sum=0
	for x in ar:
		sum += x
		print(sum)
	return sum

def compareTriplets(a, b):
    result=[0, 0]
    for x in range(0, len(a)):
        if(a[x] > b[x]):
            result[0] += 1
        if(b[x] > a[x]):
            result[1] += 1
    return result

A = [[-2, 4, 5], 
     [5, 8, 9], 
     [7, 2, 3]]

B = [[2, 3, 1, 4, 5], 
     [5, 4, 1, 8, 9], 
     [7, 6, 8, 2, -3],
     [1, 8, 9, 5, -3],
     [7, 6, 5, 1, -3]]

def diagonalDifference(arr):
    side_length = len(arr)
    a=b=count = 0
    for x in arr:
        a+=x[count]
        count+=1
    count=side_length-1
    for x in arr:
        b+=x[count]
        count-=1
    return abs(a-b)



def plus_minus(arr):
    positive=negative=zero=0
    length=len(arr)
    for i in arr:
        if(i>0):
            positive+=1
        if(i<0):
            negative+=1
        if(i==0):
            zero+=1
    positive=round(positive/length,6)
    negative=round(negative/length,6)
    zero=round(zero/length,6)

    return positive,negative,zero


def staircase(levels):
    stair="#"
    space=" "
    for x in range(1, levels+1):
        print(space*(levels-x) + stair*x)



def pyramid(levels):
    stair="#"
    space=" "
    for x in range(1, levels+1):
        print(space*(levels-x) + stair*x + stair*x + space*(levels-x))


def min_and_max_sum(arr):
    list.sort(arr)
    min_count=max_count=0
    for x in arr:
        max_count+=x

    max_count-=arr[0]
    arr.pop()

    for x in arr:
        min_count+=x
    print(min_count,max_count)


if __name__ == "__main__":
    min_and_max_sum([2,1,3,4,5])
