"""
List Manipulation
https://towardsdatascience.com/python-basics-6-lists-and-list-manipulation-a56be62b1f95


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

"""
Numpy array vs lists: https://learnpython.com/blog/python-array-vs-list/



List Comprehension
https://blog.teamtreehouse.com/python-single-line-loops

"""



"""
Iterating intelligently:

https://docs.python.org/3/library/itertools.html

https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/
"""




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
map()

A way to transform each item in an interable w/o having to pull out a loop. Creates a map function somewhere. Also faster than it's equivalent in for loops.

* can also use lambda expression like in sort() *

map(func, list)

ex: map(int, list), map(list, string), map(list, list_w_items)

"""

def digital_root_mine(n):
    if n < 10:
        return n
    else:
        return digital_root( sum( [int(x) for x in list(str(n))] ) )

def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))
