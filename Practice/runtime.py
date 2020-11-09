"""
Big-O Anal

▪ Ideal algorithm - O(1) - Linear Search, Binary Search,
    Bubble Sort, Selection Sort, Insertion Sort, Heap Sort, Shell Sort.
▪ Logarithmic - O(log n) - Merge Sort.
▪ Linear algorithm - O(n) - Quick Sort.
▪ Linearithmic - O(n * log n)
▪ Sub-linear algorithm - O(n+k) - Radix Sort.
▪ Quadratic algorithm - O(n2) 	Selection sort

* Big(O) is upper bound of runtime. *


Log(n) and n*log(n) never really made sense to me...

Logarithm - the inverse of an exponential function. 2^x --> log2x. Mirror image of exponential on a graph

*Most common attribute* - multiple choices to choose from, only need to pick one.
Most common example - phone book, don't need to loop through entire book, just go by alphabet
Runtime - Time goes up linearly while n (search space) goes up logarithmically.


*Anything w/ log(n) (in terms of sorting functions) will usually only apply to datasets that are already sorted / datasets we already have info on.

*Merge Sort (n log n)

https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/visualize/

(n log n) because


"""








"""
EXAMPLES
"""
"""
too slow, runs a sum() interates the whole list every iteration
times out 12000ms
"""
def parts_sums(ls):
    sums=[]
    for x in range(len(ls)):
        sums.append(sum(ls))
        ls.pop(0)
    sums.append(0)

    return sums

"""
faster, O(1) in O(n)
finishes all 15 tests <5000ms
"""
def parts_sums(ls):
    total = sum(ls)
    sums=[total]
    for x in ls:
        total -= x
        sums.append(total)

    return sums
