"""
CodeSignal:
-groupingDishes
    - efficiency review

-containsCloserNumber
    - literally fucking my runtime with zip()...

-rotateImage
    - review how O(1) runtime is achieved
"""


"""
Vectra CodeSignal:

1. easy one
2. file fileNaming
3. crossword / find number of words in 2d matrix


from collections import defaultdict
def fileNaming(names):
    d=defaultdict(int)
    ans=[]
    for x in names:
        d[x]+=1
        if x in d and d[x]>1:
            add=x+"({})".format(d[x])
            ans.append(add)
        else:
            ans.append(x)

    print(d)
    return ans

"""
