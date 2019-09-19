#Given a string, find the length of the longest substring without repeating characters.


def main(string):
	curr = ""
	track = []
	highest = []
	count = 0
	for x in string:
	    if(x in track):
	        highest.append(count)
	        track.clear()
	        track.append(x)
	        count = 1
	        print('if')
	        print(x, count, "\n")
	    else:
	        track.append(x)
	        count+=1
	        print('else')
	        print(track)
	        print(x, count, "\n")	   

	print(highest)
	return max(highest)


print(main("bbbbb"))