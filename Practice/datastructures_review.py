"""
Hash Tables
- python dicts, key-value pair stored in the index of an array

Insertion and search operations are very fast regardless of the size of the dataset.
Hash tables have fast runtimes b/c each value is associated with it's own unique key.
The runtime is typically O(1), just computing the index using the hash function.

What happens when using a hash table (at a high level)?

1. Insertion: The objective is to associate a key (for example someone's name)
with any kind of value/values and store it for later use.
The key-value pairs are stored in an array.
When a new pair is added to a hash table, a calculation (hash function)
is performed to determine a unique address or index of the array
for the pair to be associated with.

3. Hashing Algorithm: The calculation applied to a key will return the index of the pair.
There are multiple different hash algorithms to choose from.
Example: index = key mod (number of addresses)

2. Look ups: Apply the hash function on the key to return the index w/ the key and values

4. Collisions: What if two different keys return the same address?
One technique is Open Addressing. For example: Linear probing will search
for the next available space if the one generated is already used.
Another technique is Chaining. Each index contains a linked list which
will continue to stack key-value pairs. The hash function returns the index
and you go through each node until you find the right key.


Ex: Sum of Pairs
More Ex:
https://stackoverflow.com/questions/5900578/how-does-collections-defaultdict-work
https://realpython.com/python-defaultdict/

Editing a dict:
https://www.programiz.com/python-programming/methods/dictionary
"""
# Regular Dictionary
name="DictTest"
d={}

# adding to a "count" dictionary.
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


"""
Trees

BST-



"""
