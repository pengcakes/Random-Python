"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
***LIST STUFF***
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""
First off, all the different TYPES of DATA STORAGE

LISTS, SETS, TUPLES

LISTS - Mutable and unordered. Items in list can be replaced or changed. Defined by [].
TUPLES - Immutable and ordered. Items in set cannot be changed or replaced. Defined by ().
SET - Mutable and unordered but w/ no duplicate items. Items in set cannot be changed or replaced. Defined by set([]).

Sample code here:
https://www.geeksforgeeks.org/difference-between-list-vs-set-vs-tuple-in-python/

SET uses add and remove instead:
https://www.datacamp.com/community/tutorials/sets-in-python

"""




"""
List Manipulation
https://towardsdatascience.com/python-basics-6-lists-and-list-manipulation-a56be62b1f95

Slice Notation:
https://stackoverflow.com/questions/509211/understanding-slice-notation

Syntax: list[start, stop, step]
"""
# index 0,1,2 = 1,2,3
# index -1,-2,-3 = 5,4,3
ls=[1,2,3,4,5]

# slices into indicies 0 - 2 (not including 2)
# [first:last]
print(ls[0:2])

# everything up to index 3
print(ls[:3])

# everything from index 2 to end
print(ls[2:])

# everything from index -2 (index 3 or value 4) to end
print(ls[-2:])

# [1, 3, 5]
print(ls[::2])

# reverses the list w/ step -1
# same effect as ls.reverse() and reversed(ls)
print(ls[::-1])


# CHECK IF LIST IS EMPTY OR NOT
if list1:
    print('y/n')


"""
Numpy array vs lists: https://learnpython.com/blog/python-array-vs-list/



List Comprehension
https://blog.teamtreehouse.com/python-single-line-loops

"""



"""
Iterating Intelligently:

https://docs.python.org/3/library/itertools.html

https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/

use * to unpact iterables in a list:

    >>> fruits = ['lemon', 'pear', 'watermelon', 'tomato']
    >>> print(fruits[0], fruits[1], fruits[2], fruits[3])
    lemon pear watermelon tomato
    >>> print(*fruits)
    lemon pear watermelon tomato



ZIP function - used for parallel iteration over two lists

** be careful of runtime. Creating the list is O(1) but running it is O(NM)
https://stackoverflow.com/questions/36877715/what-is-the-time-complexity-of-zip-in-python
"""

strings=["cat", "dog", "dog"]
patterns=["a", "b", "b"]

for x,y in zip(strings, patterns):
    print(x,y)

print(tuple(zip(strings, patterns)))
print(type(zip(strings, patterns)))


# you can also use them together to transpose a 2D array

transposed_zip_file = zip(*list)



"""
ENUMERATE()
"""
strings=["cat", "dog", "dog"]
for count, value in enumerate(strings):
    print(count," ",value)

"""
any()
check if a condition holds for any out of many (an iterable)
https://stackoverflow.com/questions/52747716/check-list-to-see-if-element-greater-than-specified-number/52747789

or it may be simpler to use:

if blah not in list:
    pass

"""

x = 22
lst = [10, 20, 30]  # do NOT use list as a variable anme

if any(y > x for y in lst):
    # do stuff with lst

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
***LIST STUFF END***
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""
DEBUGGING


use assert
"""
x=12
y="12"

# print statement won't catch this ^^
# below will raise an assert error, faster and easier than printing
# won't do anything if true.
assert x==y



"""
PYTHON IMPORTS

"""
from runtime_comparison import *
from runtime_comparison import compare_runtime
import runtime_comparison as rc

Numbers and Version Diffs
"""
# Floor division - rounds down
//

# or
import math
math.floor(x)
math.ceil(x)

"""
sorted()

I'll state the obvious up front: sorted() returns a list of sorted elements and if we want to sort in a particular way or if we want to sort a complex list of elements (e.g. nested lists or a list of tuples) we can invoke the key argument.

Lambda is a one time use function used to sort a list.

adder_lambda = lambda parameter1,parameter2: parameter1+parameter2
def adder_regular(parameter1, parameter2): return parameter1+parameter2

"""

def move_zeros(array):
    new=[]
    zeros=0
    for x in array:
        if x==0  and x is not False:
            zeros+=1
        else:
            new.append(x)
    for x in range(zeros):
        new.append(0)

    return new

def move_zeros1(array):
    return sorted(array, key=lambda x: x == 0 and x is not False)


"""
map()

A way to transform each item in an interable w/o having to pull out a loop. Creates a map function somewhere. Also faster than it's equivalent in for loops.

* can also use lambda expression like in sort() *

map(func, list)

ex: map(int, list), map(list, string), map(list, list_w_items)

https://www.w3schools.com/python/ref_func_map.asp
"""

def digital_root_mine(n):
    if n < 10:
        return n
    else:
        return digital_root( sum( [int(x) for x in list(str(n))] ) )

def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))




"""
More Sorting
https://docs.python.org/3/howto/sorting.html
https://www.programiz.com/python-programming/methods/built-in/sorted
"""
def order_weight(strng):

    usable_og_string = strng.split()

    sums=[]
    for x in usable_og_string:
        sums.append( sum([int(y) for y in list(x)]) )

    # way to keep track b/c idk what else
    new_list=[]
    for x in range(0, len(usable_og_string)):
        new_list.append([sums[x], usable_og_string[x]])

    new_list.sort()

    return " ".join([x[1] for x in new_list])


def order_weight(_str):
    return ' '.join(sorted( sorted(_str.split(' ')), key=lambda x: sum(int(c) for c in x) ) )



"""
Python Sets

-contains immutable and unique items
-the set itself is mutable

create an empty set: a = set()


"""

# ADD FUNCTION ONLY ADDS IF ITEM IS NOT IN LIST

def sum_pairs(lst, s):
    cache = set()
    for i in lst:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)

# SAVES RUNTIME NOW YOU DON'T HAVE TO HAVE THE CONDITIONALS

def sum_pairs(ints, s):
    parsed=[]
    for x in ints:
        if x in parsed and x*2 != s:
            pass
        elif (s-x) in parsed:
            return [s-x, x]
        parsed.append(x)
    return None


"""
NUMPY - Use it

https://towardsdatascience.com/10-numpy-functions-you-should-know-1dc4863764c5

"""
