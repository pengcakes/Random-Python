
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
