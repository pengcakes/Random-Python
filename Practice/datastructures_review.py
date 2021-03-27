"""
Hash Tables
- python dicts, key value lookup

Ex: Sum of Pairs
More Ex:
https://stackoverflow.com/questions/5900578/how-does-collections-defaultdict-work
https://realpython.com/python-defaultdict/

Editing a dict:
https://www.programiz.com/python-programming/methods/dictionary
"""
# REGULAR DICT FIRST

name="DictTest"
d={}

# checking if key is already in dict
for x in name:
    if x not in d:
        d[x]=1
    else:
        d[x]+=1

print(d)

# DefaultDict

from collections import defaultdict

# any new key gets a default value of zero.
# wont raise KeyError (error that raises when you try to get a key not in the dict)
dd=defaultdict(int)

for x in name:
    dd[x]=+1

print(dd)


# can also sepecify default value
# same as above, but starting at 2 instead of zero
dd2= defaultdict(lambda:2)
