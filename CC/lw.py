import re

def LongestWord(sen): 

	#removes non alphanumeric numbers
  sen = re.sub(r'([^\s\w]|_)+', '', sen)
  print(sen)
  arr = sen.split(" ")


  # the list max function will return the element in arr
  # with the longest length because we specify key=len
  return max(arr, key=len)
    
print(LongestWord("the $$$longest# word is thisonemyguy"))
