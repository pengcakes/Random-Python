#longest word

var = 'one two three'
def LongestWord(sen):	
    
    for word in sen.split():
    	arr = []
    	arr.append(word)
    	#print(word)

    # code goes here 
    return arr


# keep this function call here  
print LongestWord(var)  
