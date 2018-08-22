import re

def LongestWord(sen): 

  sen = re.compile("[^a-zA-Z]")

  # now we separate the string into a list of words
  arr = sen.split(" ")

  # the list max function will return the element in arr
  # with the longest length because we specify key=len
  return max(arr, key=len)
    
print(LongestWord("the $$$longest# word is thisonemyguy"))